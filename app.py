from colony import colony_stats, calculate_reps
from flask import Flask, render_template, redirect, request
import json

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

    for nation in colony_stats["Nations"]:
        total_population = total_population + int(nation["Citizens"])
        total_wealth = total_wealth + nation["Wealth"]   
    for union in colony_stats["Unions"]:
        total_wealth = total_wealth + union["Reserve"]  
    total_population, total_wealth = f"{total_population / 1000:.3f}B", f"${total_wealth:.2f}T"

    nation_enumeration, union_enumeration = enumerate(colony_stats["Nations"]), enumerate(colony_stats["Unions"])

    return render_template('stats.html', 
                           colony_stats=colony_stats, 
                           total_population=total_population, 
                           total_wealth=total_wealth, 
                           nation_enumeration=nation_enumeration, 
                           union_enumeration=union_enumeration)

@app.post('/stats/save')
def save_stats():

    new_stats = request.data.decode('utf-8').replace('\\n', '').strip()
    new_stats = json.loads(new_stats)

    for cell in new_stats:
        new_cell_data = new_stats[cell]
        entity_index, entity_type, column = cell.split()
        entity_index = int(entity_index)
        if entity_type == "Unions":
            money_name = "Reserve"
        else:
            money_name = "Wealth"

        # entity_index = "N/A"
        # for index, nation in enumerate(colony_stats["Nations"]):
        #     print(nation["Name"], entity)
        #     if nation["Name"] == entity:
                
        #         entity_type = "Nations"
        #         money_name = "Wealth"
        #         entity_index = index
        #         break
        # if entity_index == "N/A":
        #     for index, union in enumerate(colony_stats["Unions"]):
        #         if union["Name"] == entity:
        #             money_name = "Reserve"
        #             entity_type = "Unions"
        #             entity_index = index
        #             break

        match column:
            case "Name":
                for index, nation in enumerate(colony_stats["Nations"]):
                    if index == entity_index:
                        for union in colony_stats["Unions"]:

                            if nation["Name"] in union["Members"]:
                                union["Members"][union["Members"].index(nation["Name"])] = new_cell_data
                            if nation["Name"] in union["Partial Members"]:
                                union["Partial Members"][union["Partial Members"].index(nation["Name"])] = new_cell_data
                        break
            case _ if column == money_name:
                new_cell_data = float(new_cell_data[1:-1])
            case "Citizens":
                new_cell_data = int(new_cell_data[:-1])
            case "Members":
                if "(Partial: " in new_cell_data:
                    new_cell_data, partial = new_cell_data.split("(Partial: ")
                    colony_stats[entity_type][entity_index]["Partial Members"] = " ".join(partial.split()).replace(")", "").split(", ")

                new_cell_data = " ".join(new_cell_data.split()).split(", ")
            case "Other":
                column = "Other Information"

        colony_stats[entity_type][entity_index][column] = new_cell_data

    calculate_reps(colony_stats)

    with open("data/stats.json", "w") as stats:
        stats.write(json.dumps(colony_stats, indent=4))
                
    return redirect("/stats")

if __name__ == '__main__':
    app.run(debug=True)