from modules import *

path = "./testimg/"
image = load_img(path + "test-1.png")

# Post Processing
blurred = blurring(image)
thresh = threshold(blurred)
mask = masking(thresh)

# Find Contours and draw 
x, y, w, h = find_contour(mask, image)

# Show image with bounding Box
show_img(image)
