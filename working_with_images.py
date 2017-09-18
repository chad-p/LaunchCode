from PIL import Image, ImageFilter
# load pillow

try:
    img = Image.open("luther.jpg")
except:
    print("Unable to load image")

print("The size of the Image is: ")
print(img.format, img.size, img.mode)

# Blur the image
blurred = img.filter(ImageFilter.BLUR)

# Display both images
img.show()
blurred.show()