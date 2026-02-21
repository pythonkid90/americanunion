import json
from pathlib import Path
from time import time
from random import uniform
from datetime import datetime, timedelta
from shutil import copyfile

def make_backup(backups_path, backup_timestamp, file, monthly=False):
    backups_path = Path(backups_path)
    file_name, dot, file_type = file.partition(".")
    file_type = dot + file_type

    backups_path.mkdir(parents=True, exist_ok=True)
    existing_backups = sorted([backup for backup in backups_path.iterdir() if backup.is_file()])

    if len(existing_backups) <= 5 or monthly:
        copyfile(f"data/{file}", f"{backups_path}/{file_name}_{backup_timestamp}{file_type}")
    if len(existing_backups) >= 5 and not monthly:
        Path(existing_backups[0]).unlink()

def sync_stats():
    try:
        with open("data/stats.json", "r") as colony_stats:
            colony_stats = json.load(colony_stats)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        with open("stats.json", "r") as colony_stats:
            colony_stats = json.load(colony_stats)

    return colony_stats

def update_stats(colony_stats):
    last_updated = datetime.strptime(colony_stats["last_updated"], "%Y-%m-%d")
    if datetime.now() - last_updated > timedelta(days=30):
        colony_stats["last_updated"] = datetime.strftime(last_updated + timedelta(days=30), "%Y-%m-%d")

        # Make monthly backups
        make_backup("data/backups/stats/monthly", colony_stats['last_updated'], "stats.json", monthly=True)
        make_backup("data/backups/maps/monthly", colony_stats['last_updated'], "colony-map.png", monthly=True)

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


def write_stats(colony_stats):    
    Path("data/").mkdir(parents=True, exist_ok=True)
    
    with open("data/stats.json", "r+") as saved_stats:
        if json.load(saved_stats) != colony_stats:
            try:
                old_timestamp = colony_stats["last_edit"]
            except KeyError:
                old_timestamp = time() - 1

            colony_stats["last_edit"] = time()

            make_backup("data/backups/stats", old_timestamp, "stats.json")

            saved_stats.seek(0)
            saved_stats.truncate()

            saved_stats.write(json.dumps(colony_stats, indent=4))

if __name__ == "__main___":
    colony_stats = sync_stats()
    update_stats(colony_stats)
    calculate_reps(colony_stats)
    write_stats(colony_stats)