import json
INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter = ",", new_line = "\n") -> list[dict]:
    with open(filename) as file:
        stuff_lines = file.readline()
        heads = stuff_lines.rstrip().split(delimiter)

        final_dict = []
        for str in file:
            every_queue = str.rstrip().split(delimiter)
            dict1 = {key: value for key, value in zip(heads, every_queue)}
            final_dict.append(dict1)

    return final_dict



print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
