# importing required libraries
import cv2
import numpy as np

# taking the input from dir
frame= cv2.imread("images/2.jpg")

# setting values for base colors
b = frame[:, :, :1]
g = frame[:, :, 1:2]
r = frame[:, :, 2:]

	# computing the mean
b_mean = np.mean(b)
g_mean = np.mean(g)
r_mean = np.mean(r)

# displaying the most prominent color
if (b_mean > g_mean and b_mean > r_mean):
	print("Blue")
	c="Blue"
elif (g_mean > r_mean and g_mean > b_mean):
	print("Green")
	c="Green"
else:
	print("Red")
	c="Red"
cv2.imshow(c, frame)

cv2.waitKey(0)
cv2.destroyAllWindows()
print()


