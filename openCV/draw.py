import cv2 as cv
from pathlib import Path
import numpy as np

blank = np.zeros((500, 500, 3), dtype="uint8")
blank[:] = 78, 106, 0
# Draw a rectangle

# cv.rectangle(blank, (0, 0), (250, 250), (0, 0, 255), 1)
cv.rectangle(blank, (0, 0), (blank.shape[1] // 2, blank.shape[0] // 2), (0, 0, 255), 1)
cv.circle(blank, (blank.shape[1] // 2, blank.shape[0] // 2), 100, (0, 0, 255), -1)


# draw a line
cv.line(blank, (0, 0), (blank.shape[1] // 2, blank.shape[0] // 2), (255, 255, 255), 3)
cv.line(blank, (500, 0), (blank.shape[1] // 2, blank.shape[0] // 2), (255, 255, 255), 3)
cv.line(blank, (0, 500), (blank.shape[1] // 2, blank.shape[0] // 2), (255, 255, 255), 3)
# cv.line(blank,(500,500), (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 255), 3)
cv.putText(
    blank, "OpenCV", (200, 380), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255, 255, 255), 2
)


cv.imshow("Blank", blank)


cv.waitKey(0)
