# load libraries
import dlib
from PIL import Image
import openface
import cv2
import numpy as np
import matplotlib.pyplot as plt

def thumbnail(img_path, predictor_path, save_path):
    # load image and detect face
    face_detector = dlib.get_frontal_face_detector()
    image = cv2.imread(img_path)
    detected_face = face_detector(image, 3)

    predictor_model = predictor_path
    face_aligner = openface.AlignDlib(predictor_model)

    for i, rect in enumerate(detected_face):
        crop_area = (rect.left(), rect.top(), rect.right(), rect.bottom())

    # edit crop_area
    ## 더하고 빼고는 임의설정이지만 이정도가 적당한듯
    croped = image[rect.top()-20:rect.bottom()+20, rect.left()-20:rect.right()+15]

    # change BGR to RGB and resize

    img_resized = cv2.resize(croped, dsize=(128,128), interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(save_path, img_resized)


    ## 결과확인
#     img_croped = cv2.cvtColor(croped, cv2.COLOR_BGR2RGB)
#     plt.imshow(img_croped, interpolation='bicubic')
    return 'crop image done'