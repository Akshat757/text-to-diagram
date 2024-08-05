import json

def parse_json(input_text):
    try:
        data = json.loads(input_text)
        return data
    except json.JSONDecodeError as e:
        raise ValueError("Invalid JSON input") from e
