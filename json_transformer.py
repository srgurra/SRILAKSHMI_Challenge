import json
import re
from datetime import datetime

def parse_bool(value):
    return value.lower() in ['1', 't', 'true']

def parse_null(value):
    return None if parse_bool(value) else None

def parse_number(value):
    try:
        return int(value.lstrip('0')) if '.' not in value else float(value)
    except ValueError:
        return None

def parse_string(value):
    value = value.strip()
    try:
        # Attempt to parse as RFC3339 date to Unix timestamp
        dt = datetime.fromisoformat(value.replace('Z', '+00:00'))
        return int(dt.timestamp())
    except ValueError:
        return value

def transform_data(data):
    result = {}
    for key, val in data.items():
        key = key.strip()
        if not key:
            continue
        
        if 'S' in val:
            transformed_value = parse_string(val['S'])
        elif 'N' in val:
            transformed_value = parse_number(val['N'])
        elif 'BOOL' in val:
            transformed_value = parse_bool(val['BOOL'])
        elif 'NULL' in val:
            transformed_value = parse_null(val['NULL'])
        elif 'L' in val:
            transformed_value = [transform_data(v) for v in val['L'] if isinstance(v, dict)]
            transformed_value = list(filter(None, transformed_value))
        elif 'M' in val:
            transformed_value = transform_data(val['M'])
        
        if transformed_value is not None:
            result[key] = transformed_value

    return result

def main():
    # Assuming JSON data is read from standard input
    input_json = json.load(sys.stdin)
    transformed_data = transform_data(input_json)
    print(json.dumps(transformed_data, indent=2))

if __name__ == '__main__':
    main()
