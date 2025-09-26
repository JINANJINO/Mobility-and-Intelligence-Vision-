import sys
import numpy as np
import cv2

image_path_list = [
    'img1.jpg',
    'img2.jpg',
    'img3.jpg'
]

imgs = []
for i in image_path_list:
    img = cv2.imread(i)
    
    if img is None:
        print('Image load failed!')
        sys.exit()
        
    imgs.append(img)
    
stitcher = cv2.Stitcher_create()
status, dst = stitcher.stitch(imgs)

if status != cv2.Stitcher_OK:
    print('Error on stitching!')
    sys.exit()
    
cv2.imwrite('result.jpg', dst)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()