def rx_json(json_obj, indent=0):
    result = []

    for key, value in json_obj.items():
        if isinstance(value, dict):
            result.append({key:type(value)})
            result.append(rx_json(value, indent + 1))
        elif isinstance(value, list):
            result.append({key:type(value)})
            for item in value:
                if isinstance(item, dict) or isinstance(item, list):
                    result.append(rx_json(item, indent + 1))
                else:
                    result.append({key:type(value)})
        else:
            result.append({key:type(value)})

    return result