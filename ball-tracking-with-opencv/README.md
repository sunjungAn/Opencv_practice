---
description: >-
  reference :
  https://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/
---

# Ball Tracking with OpenCV

## The Objectives of a project

Detect the presence of colored ball, track the ball as it moves around in the videw frames. 

#### My Github Code

{% page-ref page="./" %}

## Using Package

```python
from collections import deque
```

Maintaining such a queue allows us to draw the "contrail" of the ball as its being tracked.

Using deque's method, we need optional argument "buffer" is the maximum size of our deque. Smaller deque will lead to a shorter tail than longer queue. --&gt; referencing "pyimagesearch", then use buffer size is 64



## Result

![](../.gitbook/assets/ball-tracking-with-opencv-result.gif)

I could see that it worked well in green object. 

I want see worked well in another color object. Despite several experiments, it was difficult to find the RGB range properly, and it was not newly designed to track objects of different colors.

The investigation found that we had to capture several images, find  the RGB range properly in the photograph, and i apply it after. 







