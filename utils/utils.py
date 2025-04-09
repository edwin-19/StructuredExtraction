import json

def write_json(json_path, data):
    with open(json_path, 'w') as jsonf:
        json.dump(data, jsonf, indent=4)