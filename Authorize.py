# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 03:03:38 2020

@author: vijay
"""
import face_recognition
import cv2


know_image=face_recognition.load_image_file("known.png")
know_encode=face_recognition.face_encodings(know_image)[0]
def authorize(img): 
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # the facial embeddings for face in input
    unknown_encode=face_recognition.face_encodings(rgb)
    if len(unknown_encode)==0:
        return 'No person Detected'
    result=face_recognition.compare_faces([know_encode],unknown_encode[0])
    if result[0]==True:
        return 'Matched'
    else:
        return 'Unknown Person'

