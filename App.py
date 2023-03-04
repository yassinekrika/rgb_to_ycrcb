import numpy as np
import cv2

image = cv2.imread('/home/yassg4mer/Project/tp_tmn/echentillonnage/original_image.bmp')

matrix = [[0.299, 0.587, 0.114], 
          [-0.169, -0.331, 0.500],
          [0.500, -0.419, -0.081]]

YCrCb = [0, 128, 128] + np.matmul(matrix, image)

print(YCrCb)