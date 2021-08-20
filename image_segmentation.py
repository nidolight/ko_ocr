# 한글자씩 자르기

import cv2
import numpy as np
from numpy.lib.shape_base import dstack

def segmentate_w(image):
    img = image.copy()
    img = cv2.copyMakeBorder(img, 1, 1, 1, 1, cv2.BORDER_CONSTANT, value=[
                             255, 255, 255])  # 패딩추가
    img[img == 0] = 1
    img[img == 255] = 0

    start_col = []
    end_col = []
    all_col = 0

    window_location = []
    toggle = False

    h, w = img.shape
    projection = np.sum(img, axis=0)  # 가로 투영
    for col in range(w):  # 범위 추정
        if projection[col] != 0:
            if projection[col-1] == 0:
                all_col += 1
            if toggle == False:
                toggle = True
                start_col.append(col)
        elif projection[col] == 0:
            if toggle == True:
                toggle = False
                end_col.append(col)
                distance = end_col[-1] - start_col[-1]
                if distance < 15:
                    start_col.pop(-1)
                    end_col.pop(-1)
                elif 15 < distance < 35:
                    toggle = True
                    end_col.pop(-1)

    if not_ko(h, w, all_col):  # 한글 아닌 경우
        return False

    count = len(end_col)
    for i in range(count):
        s = start_col.pop(0)
        e = end_col.pop(0)
        window_location.append([s, 0, e-s, h])

    return window_location

def not_ko(h, w, all_col):
  n = w / h
  N = all_col  # 추정 단어 수
  if w < 150:
    if N > n + 2:
        return True
    else:
        return False

def segmentate_h(image):
    img = image.copy()
    img[img == 0] = 1
    img[img == 255] = 0

    h, w = img.shape
    h_start = 0
    h_end = h
    projection = np.sum(img, axis=1)  # 세로 투영
    for row in range(h):  # 범위 추정
        if projection[row] != 0 and projection[row-1] == 0:
            h_start= row
            break
    for row in range(h):
        if projection[h - row -1] != 0 :
            h_end = h - row -1
            break

    dst = image[h_start:h_end, 0:w]
    dst = cv2.copyMakeBorder(dst, 5, 5, 5, 5, cv2.BORDER_CONSTANT, value=[
                             255, 255, 255])  # 패딩추가

    return dst
