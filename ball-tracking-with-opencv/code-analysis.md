---
description: 'https://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/'
---

# Code Analysis



```python
greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)
pts = 64
```

define the green's range \(29, 86, 6\) ~ \(64, 255, 255\)

pts is buffer maximum size, i use 64 dequeue's size  

```python
blurred = cv2.GaussianBlur(frame, (11, 11), 0)
hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
```

For processing the frame faster, blur the frame to reduce high frequency noise and allow to focus on the structural objects inside the frame. 

