from graphviz import Digraph
import os

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
    Generates a PNG image of the parse tree and returns the path to the file.
    """
    global node_counter
    node_counter = 0  # Reset counter for each tree
    
    dot = Digraph(comment='Parse Tree')
    dot.attr('node', shape='circle', style='filled', fillcolor='lightblue', color='skyblue')
    dot.attr('edge', color='gray')
    dot.attr(rankdir='TB', size='8,5') # Top-to-Bottom layout
    
    if tree:
        _generate_dot_nodes(tree, dot)
    
    # Render the graph to a file without trying to open it, and return the path
    try:
        # The .render() method saves the file and returns its name.
        # We ensure the directory exists before saving.
        output_directory = os.path.dirname(filename)
        if output_directory and not os.path.exists(output_directory):
            os.makedirs(output_directory)

        # Remove view=True and store the path
        output_path = dot.render(filename, format='png', cleanup=True)
        print(f"✅ Successfully generated parse tree at: {output_path}")
        return output_path # Return the path for Streamlit to use
        
    except Exception as e:
        print(f"Error rendering graph: {e}")
        # Add this for better debugging on deployment platforms
        print("Please ensure the Graphviz executable is installed and in the system's PATH.")
        print("For Streamlit Cloud, add 'graphviz' to your packages.txt file.")
        return None # Return None if rendering fails
