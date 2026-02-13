from api.pythonapi.helpers import keep_digits, parse_cell_data
from api.pythonapi.update_stats import sync_stats, update_stats, calculate_reps, write_stats, make_backup
from static_routes import static

from flask import Flask, render_template, request, send_from_directory, abort
from werkzeug.security import check_password_hash
import json
import time

app = Flask(__name__)
app.register_blueprint(static)

@app.route('/data/<filename>')
def get_file(filename):
    try:
        return send_from_directory("data", filename)
    except FileNotFoundError:
        abort(404)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create')
def createdocument():
    return render_template('createdocument.html')

@app.route('/stats')
def stats():
    colony_stats = sync_stats()
    update_stats(colony_stats)

    total_population = sum(keep_digits(nation["Citizens"], float_allowed=True) for nation in colony_stats["Nations"])

    nation_wealth = sum(keep_digits(nation["Wealth"], float_allowed=True) for nation in colony_stats["Nations"])
    union_wealth = sum(keep_digits(union["Reserve"], float_allowed=True) for union in colony_stats["Unions"])
    total_wealth = nation_wealth + union_wealth
   
    total_population, total_wealth = f"{total_population / 1000:.3f}B", f"${total_wealth:.2f}T"

    return render_template('stats.html', 
                           colony_stats=colony_stats, 
                           total_population=total_population, 
                           total_wealth=total_wealth, 
                           nation_enumeration=enumerate(colony_stats["Nations"]), 
                           union_enumeration=enumerate(colony_stats["Unions"]))

@app.post('/stats/save')
def save_stats():
    colony_stats = sync_stats()
    new_stats = request.data.decode('utf-8').replace('\\n', '').strip()

    try:
        new_stats = json.loads(new_stats)
    except json.decoder.JSONDecodeError:
        return "Invalid Input", 400

    parse_cell_data(colony_stats, new_stats)

    calculate_reps(colony_stats)
    write_stats(colony_stats)

    with open("data/stats.json", "w") as stats:
        json.dump(colony_stats, stats, indent=4)
                
    return "Success", 200

@app.delete('/stats/delete/<entity_type>/<row_id>')
def delete_stats(entity_type, row_id):
    try:
        colony_stats = sync_stats()
        del colony_stats[entity_type.capitalize()][int(row_id)]
        write_stats(colony_stats)
    except IndexError:
        return "Index out of range", 400
    except ValueError:
        return "Invalid entity type or row ID", 400

    return "Success", 200


@app.post('/stats/internal_update')
def internal_update_stats():
    correct_password_hash = "scrypt:32768:8:1$guFFzZ42WveesVX4$c9e6d6d3bdb0370a953f10733afd5a74353b91c2c671fb15158c619f88436af9a98be76331d60fe1869ff128db1f499ccc6ae813468b0d7ea278d77246797602"
    if check_password_hash(correct_password_hash, request.form["password"]):
        colony_stats = sync_stats()

        new_stats = dict(request.form)
        del new_stats["password"]

        print(new_stats, "DGTY")

        for new_data in new_stats:
            try:
                new_stats[new_data] = float(new_stats[new_data])
                if new_stats[new_data].is_integer():
                    new_stats[new_data] = int(new_stats[new_data])
            except ValueError:
                pass
            
            match len(new_data.split(maxsplit=2)):
                case 3:
                    entity_index, entity_type, key = new_data.split(maxsplit=2)
                    entity_type = entity_type.capitalize()
                    colony_stats[entity_type][int(entity_index)][key] = new_stats[new_data]
                case 2:
                    entity_index, entity_type = new_data.split(maxsplit=1)
                    entity_type = entity_type.capitalize()
                    colony_stats[entity_type][int(entity_index)] = new_stats[new_data]
                case 1:
                    try:
                        colony_stats = dict(new_data)
                    except ValueError:
                        key = new_data
                        colony_stats[key] = new_stats[new_data]
                    
        calculate_reps(colony_stats)
        write_stats(colony_stats)
    else:
        return "Unauthorized", 401

    return "Success", 200

@app.post('/stats/map_upload')
def upload_map():
    request.files["new-colony-map"].save("data/colony-map.png")

    make_backup("data/backups/maps", "before_" + str(time.time()), "colony-map.png")

    return "Success", 200

if __name__ == '__main__':
    app.run(debug=True)