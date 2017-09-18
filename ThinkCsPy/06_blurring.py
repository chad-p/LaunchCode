import image
import sys
import random

img = image.Image("luther.jpg")
new_img = image.EmptyImage(img.getWidth(), img.getHeight())
win = image.ImageWin(img.getWidth(), img.getHeight())

for i in range(1, img.getWidth() - 1):
    for j in range(1, img.getHeight() - 1):
        # TODO: Randomly choose the coordinates of a neighboring pixel
        pix_x = i + random.randint(-1, +1)
        pix_y = j + random.randint(-1, +1)

        get_neighbor_pix = img.getPixel(pix_x, pix_y)

        # TODO: in the new image, set this pixel's color to the neighbor's color
        new_img.setPixel(i, j, get_neighbor_pix)

new_img.draw(win)
win.exitonclick()