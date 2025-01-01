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

# Helper function to format the ordinal suffix
def ordinal_suffix(num):
    """Return ordinal suffix for a number (1st, 2nd, etc.)."""
    if 10 <= num % 100 <= 20:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(num % 10, "th")
    return f"{num}{suffix}"

for i in range(1, 16):
    #background_color = generate_random_color()
    background_color = "#555555"
    #text_color = calculate_opposite_color(background_color)
    text_color = "#FFFFFF"
    title = ordinal_suffix(i)
    
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
    filename = f"{i:02d}_{title}.html"
    with open(filename, "w") as file:
        file.write(html_content)

print("15 HTML files generated successfully.")
