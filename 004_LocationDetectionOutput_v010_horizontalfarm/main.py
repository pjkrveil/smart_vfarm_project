from modules import *

# Declare Variables
f_type = "h"
load_path = "./testimg/"
save_path = "./result/"
filename = "test-3.png"
#filename = "test-7.jpg"
radius, l_range, h_range = 11, 205, 255
ratio = 160 / 130

mod = Modules()
# image = mod.load_img(load_path + filename)
image = mod.load_img(load_path + filename)

# Pre Processing
mask = mod.preProcessing(image, radius, l_range, h_range, f_type)

# Find Contours and draw 
location_list = mod.find_contour(mask, image, f_type)

# Extract & save the location data
image = mod.extract_data(location_list, ratio, image, save_path, filename, f_type)
# Output unit : mm
# Origin is the lefttop cornor (0, 0)

# Show image with bounding Box
mod.im_write(image, save_path, filename)
mod.show_img(image)
