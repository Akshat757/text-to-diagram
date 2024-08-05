def generate_orgchart(data):
    nodes = data.get("nodes", [])
    hierarchy = data.get("hierarchy", [])
    dot = "digraph OrgChart {\n"
    for node in nodes:
        dot += f'    {node["id"]} [label="{node["label"]}"];\n'
    for relation in hierarchy:
        dot += f'    {relation["manager"]} -> {relation["subordinate"]};\n'
    dot += "}"
    return dot
