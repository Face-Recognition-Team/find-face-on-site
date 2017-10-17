#!/usr/bin/python
import sys
import os
import dlib
import glob
from image_downloader import download_images

from scipy.spatial import distance
from skimage import io

predictor_path = "shape_predictor_68_face_landmarks.dat"
face_rec_model_path = "dlib_face_recognition_resnet_model_v1.dat"
faces_folder_path = "photos"
TRESHOLD = 0.6

def initialize():
    global detector, sp, facerec
    detector = dlib.get_frontal_face_detector()
    sp = dlib.shape_predictor(predictor_path)
    facerec = dlib.face_recognition_model_v1(face_rec_model_path)

def extract_features(face, img):
    shape = sp(img, face)
    return facerec.compute_face_descriptor(img, shape)

def extract_faces(img):
    dets = detector(img, 1)
    return dets

def get_photo_desc(img):
    face = extract_faces(img)[0]
    return extract_features(face, img)

def get_images(path):
    images = {}
    for name in os.listdir(path):
        img = io.imread(path + '/' + name)
        images[name[:name.index('.')]] = img
    return images

def is_face_recognized(face_vec, default_vec):
    return distance.euclidean(face_vec, default_vec) < TRESHOLD
    
def analyze(image_name, candidate_features, photo_features):
    dist = distance.euclidean(candidate_features, photo_features) 
    if dist < TRESHOLD:
        print('Your face found on image {} with dist {}'.format(image_name, dist))
    else:
        #print ('Definetly not your face on {} with dist {}'.format(image_name, dist))
        pass

def analyze_images(photo_desc):
    images = get_images(faces_folder_path)
    for image_name in images:
        image = images[image_name]
        faces = extract_faces(image)
        for face in faces:
            feature = extract_features(face, image)
            analyze(image_name, feature, photo_desc)
            
def main():
    initialize()
    download_images('http://www.e1.ru')

    photo = io.imread(sys.argv[1])
    photo_descriptor = get_photo_desc(photo)

    analyze_images(photo_descriptor)


if __name__ == "__main__":
    main()
