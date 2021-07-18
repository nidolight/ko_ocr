import cv2
import numpy as np

def segmentate(image):
    img = image.copy()
    img[img == 0] = 1
    img[img == 255] = 0
    start_col = []
    end_col = []
    window_location = []
    toggle = False

    h, w = img.shape
    horizontal_projection = np.sum(img, axis = 0);
    for col in range(w):  #범위 추정
        if horizontal_projection[col] != 0:
            if toggle == False:
                toggle = True
                start_col.append(col)

        elif horizontal_projection[col] == 0:
            if toggle == True:
                toggle = False
                end_col.append(col)


    count = len(end_col)
    for i in range(count):
        s = start_col.pop(0)
        e = end_col.pop(0)
        window_location.append([s, 0, e-s, h])

    return window_location