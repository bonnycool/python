import matplotlib.pyplot as plt
from PIL import Image , ImageFilter

# Open and display the created image
img = Image.open("rectangle_example.png")
#plt.imshow(img)
#plt.axis("off")  # Hide the axis
#plt.show()  # Display the image
gimg=img.convert('L')
edge=img.filter(ImageFilter.FIND_EDGES)
gimg.show()
edge.show()

