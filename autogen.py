import random

def generate_random_color():
    """Generate a random hex color."""
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

def calculate_opposite_color(hex_color):
    """Calculate the opposite color for the given hex color."""
    # Convert hex to RGB
    rgb = tuple(int(hex_color[i:i+2], 16) for i in (1, 3, 5))
    # Calculate the opposite RGB
    opposite_rgb = tuple(255 - x for x in rgb)
    # Convert back to hex
    return "#{:02x}{:02x}{:02x}".format(*opposite_rgb)

for i in range(1, 11):
    background_color = generate_random_color()
    text_color = calculate_opposite_color(background_color)
    title = f"I'm the {i}{'st' if i == 1 else 'nd' if i == 2 else 'rd' if i == 3 else 'th'} tab"
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{title}</title>
        <style>
            body {{
                background-color: {background_color};
                color: {text_color};
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                font-family: Arial, sans-serif;
                font-size: 3em;
            }}
        </style>
    </head>
    <body>
        {title}
    </body>
    </html>
    """
    
    # Save the HTML file
    with open(f"tab_{i}.html", "w") as file:
        file.write(html_content)

print("HTML files generated successfully.")
