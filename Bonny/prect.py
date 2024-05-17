from PIL import Image, ImageDraw  # Import Pillow modules

# Create a blank image with a white background
img = Image.new("RGB", (400, 200), "white")

# Create a drawing object to draw on the image
draw = ImageDraw.Draw(img)

# Draw the full rectangle (white background)
draw.rectangle([0, 0, 400, 200], outline="black")

# Draw the left half and fill with red
draw.rectangle([0, 0, 200, 200], fill="red", outline="black")

# Draw the right half and fill with blue
draw.rectangle([200, 0, 400, 200], fill="blue", outline="black")

# Save the image to a file
img.save("rectangle_example.png")  # Save the image as a PNG file
