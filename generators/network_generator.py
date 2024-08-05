def generate_network(data):
    nodes = data.get("nodes", [])
    connections = data.get("connections", [])
    dot = "graph Network {\n"
    for node in nodes:
        dot += f'    {node["id"]} [label="{node["label"]}"];\n'
    for conn in connections:
        dot += f'    {conn["from"]} -- {conn["to"]};\n'
    dot += "}"
    return dot
