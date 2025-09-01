# visualizer.py
from graphviz import Digraph

# A simple counter to ensure every node has a unique ID
node_counter = 0

def _generate_dot_nodes(node, dot):
    """Recursively traverses the tree to generate DOT language nodes and edges."""
    global node_counter
    node_id = str(node_counter)
    node_counter += 1

    # Create a label for the node (operator or number)
    label = str(node.value) if node.value is not None else node.type
    dot.node(node_id, label)

    # Recursively add children and edges
    for child in node.children:
        child_id = _generate_dot_nodes(child, dot)
        dot.edge(node_id, child_id)
        
    return node_id

def visualize_tree(tree, filename='parse_tree'):
    """
    Generates a PNG image of the parse tree.
    """
    global node_counter
    node_counter = 0  # Reset counter for each tree
    
    dot = Digraph(comment='Parse Tree')
    dot.attr('node', shape='circle', style='filled', fillcolor='lightblue')
    dot.attr(rankdir='TB', size='8,5') # Top-to-Bottom layout
    
    if tree:
        _generate_dot_nodes(tree, dot)
    
    # Render the graph to a file and open it
    try:
        output_path = dot.render(filename, view=True, format='png', cleanup=True)
        print(f"✅ Successfully generated parse tree at: {output_path}")
    except Exception as e:
        print(f"Error rendering graph: {e}")
        print("Please ensure Graphviz is installed and in your system's PATH.")
        print("Installation instructions: https://graphviz.org/download/")