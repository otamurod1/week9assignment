def parse_tag(tag_string, required_labels):
    if not tag_string.endswith('*'):
        return "Error: Read error."

    cleaned = tag_string[:-1]
    parts = cleaned.split('/')
    data = {}
    for part in parts:
        if '#' in part:
            label, value = part.split('#', 1)
            data[label] = value

    missing = []
    for label in required_labels:
        if label not in data:
            missing.append(label)

    if missing:
        return f"Error: Missing labels: {missing}" 

    result = []
    for label in required_labels:
        result.append(data[label])

    return result

scan1 = "SKU#TX-99/LOC#Row3/BATCH#B7*"
req1 = ["SKU", "LOC", "BATCH"]
print(parse_tag(scan1, req1))

scan2 = "SKU#RX-11/LOC#Row1*"
req2 = ["SKU", "LOC", "BATCH"]
print(parse_tag(scan2, req2))

scan3 = "SKU#ZZ-00/LOC#Dock"
req3 = ["SKU"]
print(parse_tag(scan3, req3))

scan4 = "EXP#2024/SKU#MILK/LOC#Fridge*"
req4 = ["SKU", "LOC", "EXP"]
print(parse_tag(scan4, req4))