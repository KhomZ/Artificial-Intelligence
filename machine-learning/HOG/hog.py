# importing required libraries

from skimage.io import imread
from skimage.transform import resize
from skimage.feature import hog
from skimage import exposure
import matplotlib.pyplot as plt

# reading the image
img = imread('cat.jpg')
plt.axis("off")
plt.imshow(img)
print(img.shape)