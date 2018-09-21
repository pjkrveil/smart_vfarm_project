from modules import *

# Declare Variables
load_path = "./testimg/"
save_path = "./result/"
filename = "test-7.jpg"

# Load Image
image = load_img(load_path + filename)

# Pre Processing
mask = preProcessing(image)

# Find Contours and draw 
location_list = find_bbox(mask, image)

# Extract & save the location data
ctr_list, image = point_ctr(location_list, image)
save_lcdata(ctr_list, save_path + "data_" + filename[:-4] + ".txt")

# Show image with bounding Box
show_img(image)
