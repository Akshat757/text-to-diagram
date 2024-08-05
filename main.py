from parsers.json_parser import parse_json
from parsers.mermaid_parser import parse_mermaid
from generators.flowchart_generator import generate_flowchart
from generators.uml_generator import generate_uml
from generators.network_generator import generate_network
from generators.orgchart_generator import generate_orgchart
from generators.erd_generator import generate_erd
from renderers.svg_renderer import render_svg
from renderers.png_renderer import render_png

def convert_to_diagram(input_text, input_format, output_format, diagram_type):
    if input_format == 'json':
        data = parse_json(input_text)
    elif input_format == 'mermaid':
        data = parse_mermaid(input_text)
    else:
        raise ValueError("Unsupported input format")

    if diagram_type == 'flowchart':
        dot_source = generate_flowchart(data)
    elif diagram_type == 'uml':
        dot_source = generate_uml(data)
    elif diagram_type == 'network':
        dot_source = generate_network(data)
    elif diagram_type == 'orgchart':
        dot_source = generate_orgchart(data)
    elif diagram_type == 'erd':
        dot_source = generate_erd(data)
    else:
        raise ValueError("Unsupported diagram type")

    output_file = f"./extras/output.{output_format}"
    if output_format == 'svg':
        render_svg(dot_source, output_file)
    elif output_format == 'png':
        render_png(dot_source, output_file)
    else:
        raise ValueError("Unsupported output format")

    return output_file

if __name__ == "__main__":
    input_text = '''{
    "entities": [
        {
            "id": "Customer",
            "name": "Customer",
            "attributes": [
                {"name": "CustomerID", "type": "int", "primaryKey": true},
                {"name": "FirstName", "type": "varchar(50)"},
                {"name": "LastName", "type": "varchar(50)"},
                {"name": "Email", "type": "varchar(100)"},
                {"name": "Phone", "type": "varchar(15)"}
            ]
        },
        {
            "id": "Order",
            "name": "Order",
            "attributes": [
                {"name": "OrderID", "type": "int", "primaryKey": true},
                {"name": "OrderDate", "type": "datetime"},
                {"name": "CustomerID", "type": "int"}
            ]
        },
        {
            "id": "Product",
            "name": "Product",
            "attributes": [
                {"name": "ProductID", "type": "int", "primaryKey": true},
                {"name": "ProductName", "type": "varchar(100)"},
                {"name": "Price", "type": "decimal(10, 2)"},
                {"name": "CategoryID", "type": "int"},
                {"name": "SupplierID", "type": "int"}
            ]
        },
        {
            "id": "Category",
            "name": "Category",
            "attributes": [
                {"name": "CategoryID", "type": "int", "primaryKey": true},
                {"name": "CategoryName", "type": "varchar(100)"}
            ]
        },
        {
            "id": "Supplier",
            "name": "Supplier",
            "attributes": [
                {"name": "SupplierID", "type": "int", "primaryKey": true},
                {"name": "SupplierName", "type": "varchar(100)"},
                {"name": "ContactName", "type": "varchar(50)"},
                {"name": "ContactPhone", "type": "varchar(15)"}
            ]
        }
    ],
    "relationships": [
        {
            "from": "Customer",
            "to": "Order",
            "type": "One-to-Many",
            "fromKey": "CustomerID",
            "toKey": "CustomerID",
            "label": "places"
        },
        {
            "from": "Order",
            "to": "Product",
            "type": "Many-to-Many",
            "joinTable": "OrderProduct",
            "fromKey": "OrderID",
            "toKey": "ProductID",
            "label": "contains"
        },
        {
            "from": "Product",
            "to": "Category",
            "type": "Many-to-One",
            "fromKey": "CategoryID",
            "toKey": "CategoryID",
            "label": "belongs to"
        },
        {
            "from": "Product",
            "to": "Supplier",
            "type": "Many-to-One",
            "fromKey": "SupplierID",
            "toKey": "SupplierID",
            "label": "supplied by"
        }
    ]
}

'''
    # "nodes": [
    #     {"id": "Start", "label": "Project Start", "shape": "ellipse"},
    #     {"id": "Planning", "label": "Planning Phase", "shape": "box"},
    #     {"id": "Design", "label": "Design Phase", "shape": "box"},
    #     {"id": "Development", "label": "Development", "shape": "box"},
    #     {"id": "Testing", "label": "Testing", "shape": "box"},
    #     {"id": "Deployment", "label": "Deployment", "shape": "box"},
    #     {"id": "End", "label": "Project End", "shape": "ellipse"},
    #     {"id": "Decision1", "label": "Decision: Design OK?", "shape": "diamond"},
    #     {"id": "Decision2", "label": "Decision: Bugs Found?", "shape": "diamond"}
    # ],
    # "edges": [
    #     {"from": "Start", "to": "Planning", "label": "Begin"},
    #     {"from": "Planning", "to": "Design", "label": "Plan Complete"},
    #     {"from": "Design", "to": "Decision1", "label": "Design Ready"},
    #     {"from": "Decision1", "to": "Development", "label": "Yes"},
    #     {"from": "Decision1", "to": "End", "label": "No"},
    #     {"from": "Development", "to": "Testing", "label": "Development Complete"},
    #     {"from": "Testing", "to": "Decision2", "label": "Testing Complete"},
    #     {"from": "Decision2", "to": "Deployment", "label": "No Bugs"},
    #     {"from": "Decision2", "to": "Development", "label": "Bugs Found"},
    #     {"from": "Deployment", "to": "End", "label": "Deployment Complete"}
    # ]

    input_format = 'json'
    output_format = 'png'
    diagram_type = 'erd'

    output_file = convert_to_diagram(input_text, input_format, output_format, diagram_type)
    print(f"Diagram saved as {output_file}")
