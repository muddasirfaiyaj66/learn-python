import cv2 as cv 
from pathlib import Path

parent_dir = Path(__file__).parent


img = cv.imread(f'{parent_dir}/assets/photos/img1.jpg')

cv.imshow('image1', img)
cv.waitKey(0)