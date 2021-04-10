import cv2
import mediapipe as mp
import math
mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

cap = cv2.VideoCapture(0)
with mp_holistic.Holistic(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as holistic:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # Flip the image horizontally for a later selfie-view display, and convert
    # the BGR image to RGB.
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    results = holistic.process(image)

    # Draw landmark annotation on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    mp_drawing.draw_landmarks(
        image, results.face_landmarks, mp_holistic.FACE_CONNECTIONS)
    j = 0
    for landmark in results.face_landmarks.landmark:
      if(j==454):
        print("rightface", landmark)
        ear1 = landmark
      elif(j==234):
        print("leftface", landmark)
        ear2 = landmark
      j+=1
    #mp_drawing.draw_landmarks(
    #    image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
    #mp_drawing.draw_landmarks(
    #    image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
    mp_drawing.draw_landmarks(
        image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)
    i = 0
    for landmark in results.pose_landmarks.landmark:
       if(i == 11):
         print("leftshoulder", landmark)
         sho1=landmark
       elif(i==12):
         print("rightshoulder", landmark)
         sho2=landmark
       i+=1

    cv2.putText(image, "ear : {}".format(math.sqrt((ear1.x-ear2.x)**2 + (ear1.y-ear2.y)**2)),(10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
    cv2.putText(image, "shoulder : {}".format(math.sqrt((sho1.x - sho2.x) ** 2 + (sho1.y - sho2.y) ** 2)), (10, 50),
                 cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    cv2.imshow('MediaPipe Holistic', image)

    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()
