import numpy as np
import cv2
import matplotlib.pyplot as plt

img_raw = cv2.imread('mandrill_colour.png')
print(type(img_raw))
img_raw.shape
plt.imshow(img_raw)

# while False:
    # cv2.imshow('mandrill', img)
# 
    # if cv2.waitKey(1) & 0xFF == 27: # If escape key pressed
        # break
# 
# cv2.destroyAllWindows()