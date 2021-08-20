# 이미지 전처리

import cv2
import numpy as np

def preprocess_word(image):
    # height, width = image.shape[:2]
    # dst = cv2.resize(image, (int(width*2), int(height*2)), interpolation=cv2.INTER_AREA)

    dst = cv2.GaussianBlur(image, (5,5),1.0)
    
    sharpening = np.array([[-1, -1, -1, -1, -1],
                         [-1, 2, 2, 2, -1],
                         [-1, 2, 9, 2, -1],
                         [-1, 2, 2, 2, -1],
                         [-1, -1, -1, -1, -1]]) / 9.0
    dst = cv2.filter2D(dst, -1, sharpening)

    ret, dst = cv2.threshold(dst, 147, 255, cv2.THRESH_BINARY)

    # delation = np.ones((3, 3), np.uint8) 
    # dst = cv2.dilate(dst, delation, iterations = 1)

    # erosion = np.ones((3, 3), np.uint8) 
    # dst = cv2.erode(dst, erosion, iterations = 1)

    return dst

def preprocess_syllable(dst):

    closing = np.ones((3, 3), np.uint8)  # dilation=>erosion
    dst = cv2.morphologyEx(dst, cv2.MORPH_CLOSE, closing)

    conv = np.array([[0, 1, 1], [0, 1, 0],[0,1,0]])
    dst = cv2.filter2D(dst, -1, conv)
    
    return dst
