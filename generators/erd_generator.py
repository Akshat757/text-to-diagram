def generate_erd(data):
    entities = data.get("entities", [])
    relationships = data.get("relationships", [])
    dot = "digraph ERD {\n"
    for entity in entities:
        dot += f'    {entity["name"]} [label="{entity["name"]}"];\n'
    for rel in relationships:
        dot += f'    {rel["from"]} -> {rel["to"]} [label="{rel["type"]}"];\n'
    dot += "}"
    return dot
