from api import sync_stats, update_stats, calculate_reps, write_stats, keep_digits
from static_routes import static

from flask import Flask, render_template, request, send_from_directory, abort
import json

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
    print(request.data, "DOGG")
    new_stats = request.data.decode('utf-8').replace('\\n', '').strip()
    new_stats = json.loads(new_stats)
    entity_index_offset = 0
    seen_entity_indices = []

    print(new_stats)
 
    for cell in new_stats:
        new_cell_data = new_stats[cell]
        entity_index, entity_type, column = cell.split()
        cell_is_new = "newCell" in entity_index
        entity_type = entity_type.capitalize()

        if cell_is_new:
            raw_entity_index = entity_index
            entity_index = int(entity_index.split("After")[1]) + 1

            if raw_entity_index not in seen_entity_indices:
                seen_entity_indices += [raw_entity_index]
                colony_stats[entity_type].insert(entity_index, {column: new_cell_data, "Rep. Ratio": 100000})
    
                entity_index_offset += 1
        else:
            entity_index = int(entity_index)

            entity_index += entity_index_offset

        match column:
            case "Name":
                if not cell_is_new:
                    for index, nation in enumerate(colony_stats["Nations"]):
                        if index == entity_index:
                            for union in colony_stats["Unions"]:
                                if nation["Name"] in union["Members"]:
                                    union["Members"][union["Members"].index(nation["Name"])] = new_cell_data
                                if nation["Name"] in union["Partial Members"]:
                                    union["Partial Members"][union["Partial Members"].index(nation["Name"])] = new_cell_data
                            break
            case "Reserve" | "Wealth":
                new_cell_data = keep_digits(new_cell_data, float_allowed=True)
            case "Reps.":
                if "(Citizen to Rep Ratio: " in new_cell_data:
                    new_cell_data, rep_ratio = new_cell_data.split("(Citizen to Rep Ratio: ")
                    citizens_per_rep, reps_per_x_citizens = rep_ratio.split(":")
                    rep_ratio = int(int(keep_digits(citizens_per_rep)) / int(keep_digits(reps_per_x_citizens)))
                    colony_stats[entity_type][entity_index]["Rep. Ratio"] = rep_ratio
            case "Citizens":
                new_cell_data = keep_digits(new_cell_data)
            case "Members":
                if "(Partial: " in new_cell_data:
                    new_cell_data, partial = new_cell_data.split("(Partial: ")
                    colony_stats[entity_type][entity_index]["Partial Members"] = " ".join(partial.split()).replace(")", "").split(", ")

                if "," in new_cell_data:
                    new_cell_data = " ".join(new_cell_data.split()).split(", ")
                else:
                    new_cell_data = [" ".join(new_cell_data.split())]
            case "Other":
                column = "Other Information"
            case "Background":
                column = "Background Color"

        colony_stats[entity_type][entity_index][column] = new_cell_data

    calculate_reps(colony_stats)
    write_stats(colony_stats)


    with open("data/stats.json", "w") as stats:
        json.dump(colony_stats, stats, indent=4)
                
    return "Success", 200

@app.delete('/stats/delete/<entity_type>/<row_id>')
def delete_stats(entity_type, row_id):
    colony_stats = sync_stats()
    del colony_stats[entity_type.capitalize()][int(row_id)]
    write_stats(colony_stats)

    return "Success", 200

if __name__ == '__main__':
    app.run(debug=True)