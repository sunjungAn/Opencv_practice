from imutils import face_utils
import numpy as np
import argparse
import imutils
import dlib
import cv2

#ap = argparse.ArgumentParser()
#ap.add_argument("-p", "--shape-predictor", required=True, help="path to facial landmark predictor")
#ap.add_argument("-i", "--image", required=True, help="path to input image")
#ap.add_argument('--draw', nargs='?', const=True, type=bool, default=False, help="Fill landmarks")
#args = vars(ap.parse_args())


detector = dlib.get_frontal_face_detector()
#standard Histogram of Oriented Gradients + Linear SVM method for object detection.
predictor = dlib.shape_predictor("./shape_predictor_68_face_landmarks.dat")

image = cv2.imread("bts.jpg")
image = imutils.resize(image, width = 500)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

rect = detector(gray, 1)

for(i, rect) in enumerate(rect):
    shape = predictor(gray, rect)
    shape = face_utils.shape_to_np(shape) # coverts object to Numpy array with(68,2)
    (x, y, w, h) = face_utils.rect_to_bb(rect) #draw bounding box surrounding the detected face
    cv2.rectangle(image, (x, y), (x+w, y+h), (0,255,0),2)
    #show the face number
    cv2.putText(image, "Face #{}". format(i +1), (x-10, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    #draw facial landmarks one image
for (x, y) in shape:
        cv2.circle(image, (x,y), 1, (0,0,255), -1)

cv2.imshow("Output", image)
cv2.waitKey(0)