def parse_mermaid(input_text):
    lines = input_text.strip().split('\n')
    diagram_type = lines[0].strip().split(' ')[1]
    elements = lines[1:]
    return {"type": diagram_type, "elements": elements}
