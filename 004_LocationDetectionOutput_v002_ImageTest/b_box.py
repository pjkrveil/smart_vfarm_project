from modules import *

# Declare Variables
load_path = "./testimg/"
save_path = "./result/"
filename = "test-7.jpg"
l_range, h_range = 100, 200

# image = mod.load_img(load_path + filename)
image = load_img(load_path + filename)

# Post Processing
mask = preProcessing(image, l_range, h_range)

# Find Contours and draw 
location_list = find_contour(mask, image)

# Extract & save the location data
image = extract_data(location_list, image, save_path + "lc_data_" + filename[:-4] + ".txt")

# Show image with bounding Box
mod.show_img(image)
