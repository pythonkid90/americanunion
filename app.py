from colony import colony_stats, calculate_reps
from flask import Flask, render_template, redirect, request
import json
from pprint import pprint

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stats')
def stats():
    return render_template('stats.html', colony_stats=colony_stats)

@app.post('/stats/save')
def save_stats():

    new_stats = request.data.decode('utf-8').replace('\\n', '').strip()
    new_stats = json.loads(new_stats)

    for cell in new_stats:
        new_cell_data = new_stats[cell]

        entity, column = cell.rsplit(maxsplit=1)

        column = column.capitalize()
        if column == "Other":
            column = "Other Information"

        if entity in colony_stats["Unions"]:
            if column == "Reps":
                column = "Reps."

            entity_type = "Unions"
            money_name = "Reserve"
        else:
            if column == "Land":
                column = "Location/Land"
            
            entity_type = "Nations"
            money_name = "Wealth"

        if column == money_name:
            new_cell_data = float(new_cell_data[1:-1])
        
        if not column == "Members" and not column == "Name":
            colony_stats[entity_type][entity][column] = new_cell_data
        elif column == "Members":
            if "(Partial: " in new_cell_data:
                members, partial = new_cell_data.split("(Partial: ")
                colony_stats[entity_type][entity]["Partial Members"] = " ".join(partial.split()).replace(")", "").split(", ")
            else:
                members = new_cell_data

            colony_stats[entity_type][entity]["Members"] = " ".join(members.split()).split(", ")

    calculate_reps()

    with open("data/stats.json", "w") as stats:
        stats.write(json.dumps(colony_stats, indent=4))
                
    return redirect("/stats")

if __name__ == '__main__':
    app.run(debug=True)