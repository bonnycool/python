from PIL import Image, ImageFilter,ImageDraw

img=Image.new("RGB",(400,200),"white")

d=ImageDraw.Draw(img)

d.rectangle([0,0,400,200],fill="red")
img.save("blurry.png")


# Open the image
image = Image.open('blurry.png')

# Define the region to blur (coordinates are in the format (left, top, right, bottom))
region = (0,200, 200, 400)

# Crop the region from the original image
cropped_region = image.crop(region)

# Apply blur filter to the cropped region
blurred_region = cropped_region.filter(ImageFilter.GaussianBlur(radius=10))

# Paste the blurred region back onto the original image
image.paste(blurred_region, region)

# Display the image with the blurred region
image.show()