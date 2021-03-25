---
description: introduce methods that we use for detected facial-landmarks
---

# what is dlib, imutils? \(+ how to install\)

## **dlib**

**reference** : \([http://dlib.net/](http://dlib.net/)\)

Dlib is a modern C++ toolkit containing machine learning algorithms and tools for creating complex software in C++ to solve real world problems.

### The Library

* Algorithms
* API Wrappers
* Bayesian Nets
* Compression
* Containers
* Graph Tools
* Image Processing
* Linear Algebra
* Machine Learning
* Metaprogramming
* Miscellaneous
* Networking
* Optimization
* Parsing

### Using methods

**dlib.get\_frontal\_face\_detector\(\)** - ****Returns the default face detector

**shape\_predictor\(\) -** This object is a tool that takes in an image region containing some object and outputs a set of point locations that define the pose of the object. The classic example of this is human face pose prediction, where you take an image of a human face as input and are expected to identify the locations of important facial landmarks such as the corners of the mouth and eyes, tip of the nose, and so forth. 

_requires_

* image is a numpy ndarray containing either an 8bit grayscale or RGB image.
* box is the bounding box to begin the shape prediction inside.

_ensures_

* This function runs the shape predictor on the input image and returns a single full\_object\_detection.



### Download dlib\(for window\)

* CMake download , pip install CMake
* 


## Imutils

 A series of convenience functions to make basic image processing functions such as translation, rotation, resizing, skeletonization, and displaying Matplotlib images easier with OpenCV and _**both**_ Python 2.7 and Python 3.

reference : [https://github.com/jrosebr1/imutils](https://github.com/jrosebr1/imutils)

> we use imutils to use webcam video, face\_utils ...etc



### Download imutils\(for window\)

* go to [https://github.com/jrosebr1/imutils](https://github.com/jrosebr1/imutils)
* git clone code in same repository with your activities source code repos
* pip install imutils







