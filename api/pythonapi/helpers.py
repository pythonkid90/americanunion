def clean_numeric_data(data, float_allowed=False):
    if float_allowed:
        whole, point, decimal = str(data).partition(".")
        whole, decimal = ''.join(filter(str.isdigit, whole)), ''.join(filter(str.isdigit, decimal))
        return float(whole + "." + decimal)
    else:
        return int(''.join(filter(str.isdigit, str(data))))

keep_digits = clean_numeric_data

def process_cell_data(colony_stats, new_stats, cell, entity_index_offset, seen_entity_indices):
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


    return new_cell_data, entity_index, entity_index_offset, entity_type, column, cell_is_new

def format_cell_data(colony_stats, new_cell_data, entity_index, entity_type, column, cell_is_new):
    match column:
        case "Name":
            if not cell_is_new:
                for index, nation in enumerate(colony_stats["Nations"]):
                    if index == entity_index and entity_type == "Nations":
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

def parse_cell_data(colony_stats, new_stats):
    entity_index_offset = 0
    seen_entity_indices = []

    for cell in new_stats:
        new_cell_data, entity_index, entity_index_offset, entity_type, column, cell_is_new = process_cell_data(colony_stats, new_stats, cell, entity_index_offset, seen_entity_indices)

        format_cell_data(colony_stats, new_cell_data, entity_index, entity_type, column, cell_is_new)