from modules import *

load_path = "./testimg/"
save_path = "./result/"
image = load_img(load_path + "test-1.jpg")

# Declare Variables

# Pre-Processing
blurred = blurring(image)
thresh = threshold(blurred)
mask = masking(thresh)

# Find Contours and draw 
location_list = find_contour(mask, image)

# Extract & save the location data
ctr_list, image = point_ctr(location_list, image)
save_lcdata(ctr_list, save_path + "lc_data.txt")

# Show image with bounding Box
show_img(image)
