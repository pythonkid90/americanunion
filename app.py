from colony import colony_stats, calculate_reps
from flask import Flask, render_template, redirect, request
import json
from pprint import pprint

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create')
def createdocument():
    return render_template('createdocument.html')

@app.route('/stats')
def stats():

    total_wealth = 0
    total_population = 0
    for nation_name in colony_stats["Nations"]:
        total_population = total_population + int(colony_stats["Nations"][nation_name]["Citizens"])
        total_wealth = total_wealth + colony_stats["Nations"][nation_name]["Wealth"]   
    for union_name in colony_stats["Unions"]:
        total_wealth = total_wealth + colony_stats["Unions"][union_name]["Reserve"]  
    total_population, total_wealth = f"{total_population / 1000:.3f}B", f"${total_wealth:.2f}T"

    return render_template('stats.html', colony_stats=colony_stats, total_population=total_population, total_wealth=total_wealth)

@app.post('/stats/save')
def save_stats():

    new_stats = request.data.decode('utf-8').replace('\\n', '').strip()
    new_stats = json.loads(new_stats)

    for cell in new_stats:
        new_cell_data = new_stats[cell]

        entity, column = cell.rsplit(maxsplit=1)

        if column == "Other":
            column = "Other Information"

        if entity in colony_stats["Unions"]:
            entity_type = "Unions"
            money_name = "Reserve"
        else:
            entity_type = "Nations"
            money_name = "Wealth"

        if column == money_name:
            new_cell_data = float(new_cell_data[1:-1])
        
        match column:
            case "Members":
                if "(Partial: " in new_cell_data:
                    members, partial = new_cell_data.split("(Partial: ")
                    colony_stats[entity_type][entity]["Partial Members"] = " ".join(partial.split()).replace(")", "").split(", ")
                else:
                    members = new_cell_data

                colony_stats[entity_type][entity]["Members"] = " ".join(members.split()).split(", ")
            case "Citizens":
                colony_stats[entity_type][entity][column] = new_cell_data[:-1]
            case "Name":
                ...
                # if new_cell_data not in colony_stats[entity_type]:
                    # colony_stats[entity_type][new_cell_data] =
            case _:
                colony_stats[entity_type][entity][column] = new_cell_data

    calculate_reps(colony_stats)

    with open("data/stats.json", "w") as stats:
        stats.write(json.dumps(colony_stats, indent=4))
                
    return redirect("/stats")

if __name__ == '__main__':
    app.run(debug=True)