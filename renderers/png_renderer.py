import pygraphviz as pgv

def render_png(dot_source, output_file):
    graph = pgv.AGraph(string=dot_source)
    graph.layout(prog='dot')
    graph.draw(output_file, format='png')
