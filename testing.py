import dlib
from PIL import Image
import cv2
import openface
from skimage import io
import keras
import numpy as np


def test(model, predictor, img):
    face_detector = dlib.get_frontal_face_detector()
    image = io.imread(img)
    detected_face = face_detector(image, 3)
    
    predictor_model = predictor
    face_aligner = openface.AlignDlib(predictor_model)

    for i, rect in enumerate(detected_face):
        crop_area = (rect.left(), rect.top(), rect.right(), rect.bottom())

    alignedFace = face_aligner.align(224, image, rect, landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)
    
    im = np.reshape(alignedFace, (1,224,224,3))/255
    
    result = list(train_gen.class_indices.keys())[np.argmax(model.predict(im))]
    
    return result
