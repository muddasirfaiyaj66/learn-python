# type:ignore
import cv2
from pathlib import Path

parent_dir = Path(__file__).parent


img = cv2.imread(f"{parent_dir}/assets/FlexSync.png", 0)
# img = cv2.resize(img, (200,200))
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
