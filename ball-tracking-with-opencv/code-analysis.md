---
description: 'https://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/'
---

# Code Analysis



```python
greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)
pts = 64
```

define the green's range \(29, 86, 6\) ~ \(64, 255, 255\). **pts** is buffer maximum size, i use 64 dequeue's size  

```python
blurred = cv2.GaussianBlur(frame, (11, 11), 0)
hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
```

For processing the frame faster, blur the frame to reduce high frequency noise and allow to focus on the structural objects inside the frame. 

```python
	mask = cv2.inRange(hsv, greenLower, greenUpper)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)
```

### **Ref**

> \*\*\*\*[**https://opencv-python-tutroals.readthedocs.io/en/latest/py\_tutorials/py\_imgproc/py\_morphological\_ops/py\_morphological\_ops.html**](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_morphological_ops/py_morphological_ops.html)\*\*\*\*

**&lt;cv2.erode\(\)&gt;**

thickness or size of the foreground object decreases or simply white region decreases in the image. It is useful for removing small white noises.

**&lt;cv2.dilate\(\)&gt;**

**It is just opposite of erosion.** erosion removes white noises, but it also shrinks our object. So we dilate it.

![cv2. erosion\(\)](../.gitbook/assets/image%20%287%29.png)

![cv2.dilation\(\)](../.gitbook/assets/image%20%285%29.png)

erosion, dilation is use to remove any small noise

```python
c = max(cnts, key=cv2.contourArea)
((x, y), radius) = cv2.minEnclosingCircle(c)
M = cv2.moments(c)
center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
```

I find the largest contour inthe cnts list. -&gt; compute minimum enclosing circle of the blob.  -&gt; compute the center _\(x, y\)_-coordinates

If complete computing \(x,y\)-coordinate, append value in dequeu "pts"

```python
thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)
```

compute the thickness of the contrail and then draw it on the frame using cv2.line\(\)







