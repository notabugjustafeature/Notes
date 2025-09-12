from graphviz import Digraph

# Create a visual wiring diagram of the basic Arduino traffic light simulator
dot = Digraph(format='png')
dot.attr(rankdir='LR', size='10')

# Nodes
dot.node('A', 'Arduino Uno\n[Digital Pins]', shape='box', style='filled', fillcolor='lightblue')
dot.node('R', 'Red LED\nPin 2', shape='circle', style='filled', fillcolor='red', fontcolor='white')
dot.node('Y', 'Yellow LED\nPin 3', shape='circle', style='filled', fillcolor='yellow')
dot.node('G', 'Green LED\nPin 4', shape='circle', style='filled', fillcolor='green', fontcolor='white')
dot.node('GR', 'GND', shape='box', style='filled', fillcolor='gray', fontcolor='white')

# Edges
dot.edge('A', 'R', label='Pin 2\n→ 220Ω Resistor → LED → GND')
dot.edge('A', 'Y', label='Pin 3\n→ 220Ω Resistor → LED → GND')
dot.edge('A', 'G', label='Pin 4\n→ 220Ω Resistor → LED → GND')

# Show all LEDs grounded
dot.edge('R', 'GR', style='dashed')
dot.edge('Y', 'GR', style='dashed')
dot.edge('G', 'GR', style='dashed')

# Save diagram
dot.render('arduino_traffic_light_diagram', cleanup=False)
