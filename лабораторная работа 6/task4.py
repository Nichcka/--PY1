import json
INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter = ",", new_line = "\n") -> list[dict]:
    with open(filename) as file:
        stuff_lines = file.readlines()
        stuff_lines = [str_.strip(new_line) for str_ in stuff_lines]

    heads = list(item for item in str(stuff_lines[0]).split(delimiter))
    first_queue = list(item for item in str(stuff_lines[1]).split(delimiter))
    second_queue = list(item for item in str(stuff_lines[2]).split(delimiter))
    third_queue = list(item for item in str(stuff_lines[3]).split(delimiter))
    forth_queue = list(item for item in str(stuff_lines[4]).split(delimiter))

    dict1 = {heads[i]: first_queue[i] for i in range(len(heads))}
    dict2 = {heads[i]: second_queue[i] for i in range(len(heads))}
    dict3 = {heads[i]: third_queue[i] for i in range(len(heads))}
    dict4 = {heads[i]: forth_queue[i] for i in range(len(heads))}

    finally_dict = [dict1, dict2, dict3, dict4]

    return finally_dict


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
