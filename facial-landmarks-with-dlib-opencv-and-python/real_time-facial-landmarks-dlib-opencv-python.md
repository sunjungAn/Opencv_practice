---
description: >-
  Practice with using dlib, imutils package
  reference(https://www.pyimagesearch.com/2017/04/03/facial-landmarks-dlib-opencv-python/)
---

# Real\_time facial-landmarks-dlib-opencv-python

## The Objectives of a project

Using a webcam, we will get real-time video. so, I will detect facial-landmakrs \(detect Eyes, Eyebows, Nose, Mouth, Jawline\).

pre-trained Linear SVM object detector specifically for the task of **face detect.**

### Result 

![image Data  &amp;lt;BTS&amp;gt;](../.gitbook/assets/result_bts.png)



### Using Methods

**face\_**_**utils.rect\_to\_bb\(rect\)** : take a bounding predicted by dlib and convert it , transforms it into 4 tuple of coordinates._

**face\_**_**utils**_**.shape\_**_**to\_**_**np\(shape\)** : we cam convert this object to Numpy array.

**dlib.face\_detector** :  [Histogram of Oriented Gradients + Linear SVM method](https://pyimagesearch.com/2014/11/10/histogram-oriented-gradients-object-detection/)

## Additional

_If you want more detailed study go to_ 

> [https://www.pyimagesearch.com/2017/04/03/facial-landmarks-dlib-opencv-python/](https://www.pyimagesearch.com/2017/04/03/facial-landmarks-dlib-opencv-python/)

If you want source code

> [https://github.com/sunjungAn/Opencv\_practice/blob/master/Facial%20landmarks%20with%20dlib%2C%20OpenCV%2C%20and%20Python/facial\_landmarks.py](https://github.com/sunjungAn/Opencv_practice/blob/master/Facial%20landmarks%20with%20dlib%2C%20OpenCV%2C%20and%20Python/facial_landmarks.py)





\_\_



