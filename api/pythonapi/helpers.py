from time import time

unions_columns = ["Name", "Leader", "Reserve", "Reps.", "Military", "Land", "Members", "Partial Members", "Other"]
nations_columns = ["Name", "Leader", "Wealth", "Citizens", "Military", "Location/Land", "Other", "Background"]

def fix_duplicate_names(duplicate_string, duplicate_count, table):
    print(duplicate_count, "1edo", time(), f"duplicate_count({duplicate_string}, {duplicate_count}, {table})")
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

def keep_digits(data, float_allowed: bool=False) -> float | int:
    if float_allowed:
        whole, point, decimal = str(data).partition(".")
        whole, decimal = ''.join(filter(str.isdigit, whole)), ''.join(filter(str.isdigit, decimal))

        if not (decimal == "" and whole == ""):
            return float(whole + "." + decimal)
        elif decimal == "" and whole != "":
            return float(whole)
        else:
            return 0.0
    else:
        data = str(data).partition(".")[0]
        return int(''.join(filter(str.isdigit, data)))

def process_cell_data(colony_stats, new_stats, cell):
    new_cell_data = str(new_stats[cell])
    entity_index, entity_type, column = cell.rsplit(maxsplit=2)
    entity_index, entity_type, column = keep_digits(entity_index.split()[0]), entity_type.title(), column.title()

    return new_cell_data, entity_index, entity_type, column

def format_cell_data(colony_stats, new_cell_data, entity_index, entity_type, column, cell_is_new):
    if column in (unions_columns if entity_type == "Unions" else nations_columns):
        match column:
            case "Name":
                # Make sure all quotes are straight and strip whitespace
                new_cell_data = new_cell_data.replace('“', '"').replace('”', '"').replace('‘', "'").replace('’', "'").replace('′', "'").replace('″', '"').strip()
                if not cell_is_new:
                    for index, nation in enumerate(colony_stats["Nations"]):
                        if index == entity_index and entity_type == "Nations":
                            for union in colony_stats["Unions"]:
                                if nation["Name"] in union["Members"]:
                                    union["Members"][union["Members"].index(nation["Name"])] = new_cell_data
                                if nation["Name"] in union["Partial Members"]:
                                    union["Partial Members"][union["Partial Members"].index(nation["Name"])] = new_cell_data
                            break

                # new_cell_data = fix_duplicate_names(new_cell_data, 1, colony_stats[entity_type])
                # print(time(), "LEINDEDO")
            case "Reserve" | "Wealth":
                new_cell_data = keep_digits(new_cell_data, float_allowed=True)
            case "Reps.":
                if "(Citizen to Rep Ratio: " in new_cell_data:
                    new_cell_data, rep_ratio = new_cell_data.split("(Citizen to Rep Ratio: ")
                    citizens_per_rep, reps_per_x_citizens = rep_ratio.split(":")
                    rep_ratio = int(keep_digits(citizens_per_rep) / keep_digits(reps_per_x_citizens))
                    colony_stats[entity_type][entity_index]["Rep. Ratio"] = rep_ratio
            case "Rep. Ratio" | "Citizens":
                new_cell_data = keep_digits(new_cell_data)
            case "Members":
                new_cell_data = new_cell_data.replace('“', '"').replace('”', '"').replace('″', '"').replace('‘', "'").replace('’', "'").replace('′', "'")

                if "(Partial: " in new_cell_data:
                    new_cell_data, partitioned, partial = new_cell_data.partition("(Partial: ")
                    colony_stats[entity_type][entity_index]["Partial Members"] = " ".join(partial.split()).removesuffix(")").split(", ")

                if "," in new_cell_data:
                    new_cell_data = " ".join(new_cell_data.split()).split(", ")
                else:
                    new_cell_data = [" ".join(new_cell_data.split())]
            case "Partial Members":
                new_cell_data = " ".join(new_cell_data.split()).split(", ")
            case "Other":
                column = "Other Information"
            case "Background":
                column = "Background Color"
                if "#" not in new_cell_data:
                    new_cell_data = "#" + new_cell_data        
        colony_stats[entity_type][entity_index][column] = new_cell_data

def parse_cell_data(colony_stats, new_stats):
    for cell in new_stats:
        new_cell_data, entity_index, entity_type, column = process_cell_data(colony_stats, new_stats, cell)

        format_cell_data(colony_stats, new_cell_data, entity_index, entity_type, column, False)

