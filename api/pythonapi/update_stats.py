import json
from pathlib import Path
from time import time
from random import uniform
from datetime import datetime, timedelta
from shutil import copyfile

def sync_stats():
    try:
        with open("data/stats.json", "r") as colony_stats:
            colony_stats = json.load(colony_stats)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        with open("stats.json", "r") as colony_stats:
            colony_stats = json.load(colony_stats)

    return colony_stats

def update_stats(colony_stats):
    print("MANNY", datetime.now() - datetime.strptime(colony_stats["last_updated"], "%Y-%m-%d"))
    last_updated = datetime.strptime(colony_stats["last_updated"], "%Y-%m-%d")
    if datetime.now() - last_updated > timedelta(days=30):
        print("okde")
        colony_stats["last_updated"] = datetime.strftime(last_updated + timedelta(days=30), "%Y-%m-%d")

        # Make monthly backup
        backups_path = Path("data/backups/monthly")
        backups_path.mkdir(parents=True, exist_ok=True)
        copyfile("data/stats.json", f"data/backups/monthly/stats_{colony_stats['last_updated']}.json")

        # Update colony wealth and citizens
        for colony in colony_stats["Nations"]:
            colony["Wealth"] += uniform(0 - colony["Wealth"] / 10, colony["Wealth"] / 10)
            colony["Wealth"] = float(f"{colony["Wealth"]:.2f}")
            
            colony["Citizens"] += int(uniform(0 - colony["Citizens"] / 20, colony["Citizens"] / 20))
        # Update union reserve
        for union in colony_stats["Unions"]:
            if union["Reserve"] != "N/A":
                union["Reserve"] += uniform(0 - union["Reserve"] / 20, union["Reserve"] / 20)
                union["Reserve"] = float(f"{union['Reserve']:.2f}")

    write_stats(colony_stats)

# Calculate union reps
def calculate_reps(colony_stats):
    for union in colony_stats["Unions"]:
        if union["Rep. Ratio"] != 0:
            total_reps = 0
            for member in union["Members"]:
                for colony in colony_stats["Nations"]:
                    if colony["Name"] == member:
                        total_reps += int(colony["Citizens"])

            total_reps *= 1000000 / union["Rep. Ratio"]
            union["Reps."] = f"{int(total_reps):,d}"
        else:
            union["Reps."] = "N/A"
    
    Path("data/").mkdir(parents=True, exist_ok=True)

def write_stats(colony_stats):    
    with open("data/stats.json", "r+") as saved_stats:
        if json.load(saved_stats) != colony_stats:
            try:
                old_timestamp = colony_stats["last_edit"]
            except KeyError:
                old_timestamp = time() - 1

            colony_stats["last_edit"] = time()

            backups_path = Path("data/backups")
            backups_path.mkdir(parents=True, exist_ok=True)
            stats_backups = sorted([backup for backup in backups_path.iterdir() if backup.is_file()])

            if len(stats_backups) <= 5:
                copyfile("data/stats.json", f"data/backups/stats_{old_timestamp}.json")
            if len(stats_backups) >= 5:
                Path(stats_backups[0]).unlink()

            saved_stats.seek(0)
            saved_stats.truncate()

            saved_stats.write(json.dumps(colony_stats, indent=4))

if __name__ == "__main___":
    colony_stats = sync_stats()
    update_stats(colony_stats)
    calculate_reps(colony_stats)
    write_stats(colony_stats)