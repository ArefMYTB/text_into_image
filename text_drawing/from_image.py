import cv2
import numpy as np

image = cv2.imread('image.jpg')
mask = cv2.imread('mask.jpg', cv2.IMREAD_GRAYSCALE)

edges = cv2.Canny(image, 100, 200)

# Apply the mask to the Canny edges
masked_edges = cv2.bitwise_and(edges, edges, mask=mask)

# cv2.imshow('Original Image', image)
# cv2.imshow('Mask', mask)
# cv2.imshow('Canny Edges', edges)
cv2.imshow('Canny Edges', masked_edges)
cv2.imwrite('canny.jpg', masked_edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
