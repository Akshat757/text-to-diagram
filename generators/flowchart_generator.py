def generate_flowchart(data):
    nodes = data.get("nodes", [])
    edges = data.get("edges", [])
    dot = "digraph G {\n"
    for node in nodes:
        dot += f'    {node["id"]} [label="{node["label"]}"];\n'
    for edge in edges:
        dot += f'    {edge["from"]} -> {edge["to"]};\n'
    dot += "}"
    return dot
