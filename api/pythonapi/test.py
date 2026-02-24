from update_stats import sync_stats
from time import time

def fix_duplicate_names(duplicate_string, duplicate_count, table):
    print(duplicate_count, "1edo", time(), f"duplicate_count({duplicate_string}, {duplicate_count})")
    if any(nation["Name"] == duplicate_string for nation in table):
        print(duplicate_count, "2edo", time())
        if duplicate_count > 0:
            print(duplicate_count, "3edo", time())
            if duplicate_string.endswith(f" ({duplicate_count - 1})"):
                duplicate_string = duplicate_string[:-2] + str(duplicate_count) + duplicate_string[-1:]

            else:
                duplicate_string += f" ({duplicate_count})"
            print(duplicate_count, "4edo", time())
            # Check to see if new string is already taken
            duplicate_string = fix_duplicate_names(duplicate_string, duplicate_count + 1, table)
    print(duplicate_count, "5edo", time())
    return duplicate_string

colony_stats = sync_stats()

print(fix_duplicate_names("Nation Name Here", 1, colony_stats["Nations"]))