import cv2
from image_deskew import deskew #return img
from image_preprocessing  import * #return img
from image_detection import detect #return ary
from image_segmentation import segmentate #return ary
from model_apply import model_apply

import numpy as np

def ko_ocr(img):
    img = deskew(img) #전처리
    img = preprocess_word(img)

    detected_location = detect(img) #영역추출
    
    # for l in detected_location:
    #     if l[2]>100 and l[3]<70 : #가로길이
    #         cv2.rectangle(img, (l[0], l[1]), ((l[0]+l[2]-1), (l[1]+l[3]-1)), (0, 255, 0),1)

    for l in detected_location:
        if l[2]>100 and l[3]<70: #한줄씩
            dst = img[l[1]: (l[1] + l[3]), l[0]: (l[0] + l[2])]
            segmentated_location = segmentate(dst) #글자단위로

            for l in segmentated_location:        
                # if(l[2] > 30 and l[3] > 30): #한글자만
                    dst2 = dst[l[1]: (l[1] + l[3]), l[0]: (l[0] + l[2])]
                    dst2 = preprocess_syllable(dst2)
                    print(model_apply(dst2), end="")
                    
                    cv2.imshow("test", dst2)
                    cv2.waitKey()   
                    cv2.destroyAllWindows()
                    
            print("")
                

def main():
    img_path = r"C:\Users\nidol\Desktop\tesseract\a5.png"
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    ko_ocr(img)

if __name__ == "__main__":
    main()
