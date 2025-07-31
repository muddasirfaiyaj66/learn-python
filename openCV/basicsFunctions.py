import cv2 as cv
from pathlib import Path

parent_path = Path(__file__).parent

img = cv.imread(f"{parent_path}/assets/photos/pic3.jpg")
img = cv.resize(img, (250, 250))
# convert to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow(" Gray Image", gray)

# blur Image
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow("Blurred Image", blur)

# Edge Cascade
canny = cv.Canny(blur, 50, 150)

cv.imshow("Canny Edges", canny)

# dialation

dilated = cv.dilate(canny, (7, 7), iterations=3)
cv.imshow("Dilated Image", dilated)

# eroding

eroded = cv.erode(canny, (7, 7), iterations=3)

cv.imshow("Eroded Image", eroded)

# Resize 
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized Image", resized)

#  cropping
cropped = img[50:200, 200:400]
cv.imshow("Cropped Image", cropped)

cv.waitKey(0)
cv.destroyAllWindows()
