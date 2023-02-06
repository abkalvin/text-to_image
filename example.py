import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Create a blank image with a size
img = Image.new("RGB", (1080, 1080), "red")

# Create a draw object to draw on the image
draw = ImageDraw.Draw(img)

# Select a font and set its size
font = ImageFont.truetype("arial.ttf", 50)

# Draw text on the image
text = "Hi hello Vanakkam Guys"
textwidth, textheight = draw.textsize(text, font)

# Calculate the position of the text
x = (img.width - textwidth) / 2
y = (img.height - textheight) / 2

# Draw the text on the image
draw.text((x, y), text, font=font, fill=(0, 0, 0))

# Save the image
img.save("hello.png")

# Show the image using matplotlib
img = np.array(img)
plt.imshow(img)
plt.show()
