import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imread, imresize

#Not we want to display 2 images, one will be tinted
img = imread('suit.jpg')
img_tinted = img * [1, 0.5, 0.9]

#Subplot function I think first argument is number of rows and second the number of columns
#and third will specify which position it should go to
plt.subplot(1,2,1)
plt.imshow(img)
plt.subplot(1, 2, 2)
plt.imshow(np.uint8(img_tinted)) #imshow is that it might give strange results
# if presented with data that is not uint8, so we explicitly cast it
plt.show()
