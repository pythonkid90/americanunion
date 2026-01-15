import json, datetime, random, pathlib

try:
    with open("data/stats.json", "r") as colony_stats:
        colony_stats = json.load(colony_stats)
except FileNotFoundError:
    with open("stats.json", "r") as colony_stats:
        colony_stats = json.load(colony_stats)

last_updated = datetime.datetime.strptime(colony_stats["last_updated"], "%Y-%m-%d")
if datetime.datetime.now() - last_updated > datetime.timedelta(days=30):
    colony_stats["last_updated"] = datetime.datetime.now().strftime("%Y-%m-%d")

    # Update colony wealth and citizens
    for colony in colony_stats["Nations"]:

        colony["Wealth"] += random.uniform(0 - colony["Wealth"] / 10, colony["Wealth"] / 10)
        colony["Wealth"] = float(f"{colony["Wealth"]:.2f}")
        
        colony["Citizens"] += int(random.uniform(0 - colony["Citizens"] / 20, colony["Citizens"] / 20))
    # Update union reserve
    for union in colony_stats["Unions"]:
        
        if union["Reserve"] != "N/A":
            union["Reserve"] += random.uniform(0 - union["Reserve"] / 20, union["Reserve"] / 20)
            union["Reserve"] = float(f"{union[f'Reserve']:.2f}")


# Calculate union reps
def calculate_reps(colony_stats):
    for union in colony_stats["Unions"]:
        if union["Reps."] != "N/A":
            total_reps = 0
            for member in union["Members"]:
                for colony in colony_stats["Nations"]:
                    if colony["Name"] == member:
                        total_reps += int(colony["Citizens"])

            total_reps *= 1000000 / union["Rep. Ratio"]
            union["Reps."] = f"{int(total_reps):,d}"

    stats_path = pathlib.Path("data/")
    stats_path.mkdir(parents=True, exist_ok=True)

    with open("data/stats.json", "w") as new_stats:
        new_stats.write(json.dumps(colony_stats, indent=4))

calculate_reps(colony_stats)