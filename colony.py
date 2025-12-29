import json, datetime, random, pprint

with open("stats.json", "r") as colony_stats:
    colony_stats = json.load(colony_stats)

last_updated = datetime.datetime.strptime(colony_stats["last_updated"], "%Y-%m-%d")
if datetime.datetime.now() - last_updated > datetime.timedelta(days=30):
    colony_stats["last_updated"] = datetime.datetime.now().strftime("%Y-%m-%d")

    # Update colony wealth and citizens
    for colony in colony_stats["Nations"]:
        colony = colony_stats["Nations"][colony]

        colony["Wealth"] += random.uniform(0 - colony["Wealth"] / 10, colony["Wealth"] / 10)
        colony["Wealth"] = float(f"{colony[f'Wealth']:.2f}")
        
        colony["Citizens"] += int(random.uniform(0 - colony["Citizens"] / 20, colony["Citizens"] / 20))


    # Update union reserve and reps
    for union in colony_stats["Unions"]:
        union = colony_stats["Unions"][union]

        if union["Reserve"] != "N/A":
            union["Reserve"] += random.uniform(0 - union["Reserve"] / 20, union["Reserve"] / 20)
            union["Reserve"] = float(f"{union[f'Reserve']:.2f}")

        if union["Reps."] != "N/A":
            total_reps = sum([colony_stats["Nations"][member]["Citizens"] for member in union["Members"]])
            total_reps *= 1000000 / union["Rep. Ratio"]
            union["Reps."] = f"{int(total_reps):,d}"

with open("new_stats.json", "w") as new_stats:
    new_stats.write(json.dumps(colony_stats, indent=4))
                