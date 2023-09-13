import tkinter as tk
from tkinter import ttk, messagebox
import networkx as nx
import matplotlib.pyplot as plt

app = tk.Tk()
app.title("ERDTool")

# NetworkX Graph Initialization
G = nx.DiGraph()

# Main frame for content
main_frame = ttk.Frame(app, padding="10")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# From Table
from_label = ttk.Label(main_frame, text="From Table:")
from_label.grid(row=0, column=0, sticky=tk.W, pady=5)
from_entry = ttk.Entry(main_frame)
from_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5)

# To Table
to_label = ttk.Label(main_frame, text="To Table:")
to_label.grid(row=1, column=0, sticky=tk.W, pady=5)
to_entry = ttk.Entry(main_frame)
to_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)

# Joining Key
key_label = ttk.Label(main_frame, text="Joining Key:")
key_label.grid(row=2, column=0, sticky=tk.W, pady=5)
key_entry = ttk.Entry(main_frame)
key_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5)

def add_to_diagram():
    from_table = from_entry.get()
    to_table = to_entry.get()
    joining_key = key_entry.get()

    # Add nodes and edges to the graph
    G.add_node(from_table, shape='rectangle')
    G.add_node(to_table, shape='rectangle')
    G.add_edge(from_table, to_table, label=joining_key)
    
    # Clean input fields for new entries
    from_entry.delete(0, tk.END)
    to_entry.delete(0, tk.END)
    key_entry.delete(0, tk.END)

    messagebox.showinfo("Info", "Relationship added!")

def show_erd():
    pos = nx.spring_layout(G)
    plt.figure(figsize=(10,6))
    
    # Draw edges and edge labels
    nx.draw_networkx_edges(G, pos, width=2)
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    # Draw nodes (as rectangles) and labels inside them
    for node, (x, y) in pos.items():
        plt.gca().add_patch(plt.Rectangle((x-0.2, y-0.1), 0.4, 0.2, fc="skyblue"))
        plt.text(x, y, node, fontsize=12, ha='center', va='center')
    
    plt.title("Entity Relationship Diagram")
    plt.axis('off')  # Hide the axis
    plt.tight_layout()
    plt.show()


add_button = ttk.Button(main_frame, text="Add to Diagram", command=add_to_diagram)
add_button.grid(row=3, column=0, columnspan=2, pady=5)

show_button = ttk.Button(main_frame, text="Show ERD", command=show_erd)
show_button.grid(row=4, column=0, columnspan=2, pady=10)

main_frame.columnconfigure(1, weight=1)

app.mainloop()
