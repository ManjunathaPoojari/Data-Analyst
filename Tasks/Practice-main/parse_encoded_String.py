def parse_encoded_string(s):
    parts = []
    current = ""
    for ch in s:
        if ch != '0':
            current += ch
        else:
            if current != "":
                parts.append(current)
                current = ""
    if current != "":
        parts.append(current)
    return {
        "first_name": parts[0],
        "last_name": parts[1],
        "id": parts[2]
    }
encoded = "Robert000Smith000123"
result = parse_encoded_string(encoded)
print(result)
