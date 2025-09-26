import numpy as np
import cv2
from matplotlib import pyplot as plt

imgL = cv2.imread('./left.png', cv2.IMREAD_GRAYSCALE)
imgR = cv2.imread('./right.png', cv2.IMREAD_GRAYSCALE)

stereo = cv2.StereoBM.create(numDisparities=64, blockSize=21)
disparity = stereo.compute(imgL, imgR)

# 깊이 정보 시각화
disparity_normalized = cv2.normalize(disparity, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
cv2.imshow("Disparity", disparity_normalized)
cv2.waitKey(0)