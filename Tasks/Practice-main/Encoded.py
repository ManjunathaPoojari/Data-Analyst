def parse_encoded_string(encoded):
    parts = encoded.split('0')
    clean_parts = [p for p in parts if p]
    return {
        "first_name": clean_parts[0],
        "last_name": clean_parts[1],
        "id": clean_parts[2]
    }
