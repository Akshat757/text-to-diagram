def generate_uml(data):
    classes = data.get("classes", [])
    relationships = data.get("relationships", [])
    dot = "digraph UML {\n"
    for cls in classes:
        dot += f'    {cls["name"]} [label="{cls["name"]}"];\n'
    for rel in relationships:
        dot += f'    {rel["from"]} -> {rel["to"]} [label="{rel["type"]}"];\n'
    dot += "}"
    return dot
