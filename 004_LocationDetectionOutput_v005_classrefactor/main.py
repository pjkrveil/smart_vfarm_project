from modules import *

# Declare Variables
load_path = "./testimg/"
save_path = "./result/"
filename = "test-7.jpg"
l_range, h_range = 200, 255

mod = Modules()
# image = mod.load_img(load_path + filename)
image = mod.load_img(load_path + filename)

# Post Processing
mask = mod.preProcessing(image, l_range, h_range)

# Find Contours and draw 
location_list = mod.find_contour(mask, image)

# Extract & save the location data
image = mod.extract_data(location_list, image, save_path + "lc_data_" + filename + ".txt")

# Show image with bounding Box
mod.show_img(image)