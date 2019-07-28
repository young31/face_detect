import dlib
from PIL import Image
import cv2
import openface
from skimage import io
import os

def crop(predictor, name, from_dir, to_dir, rename=True):
    face_detector = dlib.get_frontal_face_detector()
    predictor_model = predcitor
    face_marks = dlib.shape_predictor(predictor_model)
    face_aligner = openface.AlignDlib(predictor_model)
    
    names = name
    path = to_dir

    if rename:
        for i, tar in enumerate(list(os.walk(from_dir))[0][2], start=1):
            os.path.join(from_dir+'/'+tar, from_dir + '/' + f'{names}.{i}.jpg')
        
    
    for i, name in enumerate(list(os.walk(from_dir))[0][2], start=1):
    try:
        fname = from_dir + '/' + f'{names}.{i}.jpg'
        image = io.imread(fname)
        detected_face = face_detector(image, 3)

        for j, rect in enumerate(detected_face):
            alignedFace = face_aligner.align(224, image, rect, landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)
            cv2.imwrite(os.path.join(path, f"{names}.{i}.jpg"), alignedFace)
    except:
        continue

