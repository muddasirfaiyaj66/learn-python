import cv2 as cv
import numpy as np

blank = np.zeros((307, 512, 3), dtype="uint8")
blank[:] = 78, 106, 0
cv.circle(blank, (250, 150), 80, (0, 0, 255), -1)
cv.imshow("Bangladesh's National Flag", blank)


cv.waitKey(0)
