import cv2

def edge_detect(path, file_name, tresh_min, tresh_max):
    image = cv2.imread(path + file_name)
    im_bw = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    thresh, im_bw = cv2.threshold(im_bw, tresh_min, tresh_max, 0)
    cv2.imwrite('./result/bw_' + file_name, im_bw)

    _, contours, hierarchy = cv2.findContours(im_bw, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(image, contours, -1, (0,255,0), 3)
    cv2.imwrite('./result/cnt_' + file_name, image)

if __name__ == '__main__':
  edge_detect('./testimg/', 'test_1.jpg', 200, 240)
  edge_detect('./testimg/', 'test_2.jpg', 200, 240)
  edge_detect('./testimg/', 'test_3.jpg', 200, 240)
  edge_detect('./testimg/', 'test_4.jpg', 200, 240)