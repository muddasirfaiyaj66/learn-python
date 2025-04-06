import cv2
from pathlib import Path
import random

parent_dir = Path(__file__).parent

img = cv2.imread(f'{parent_dir}/assets/FlexSync.png',1)

print(img)
print(type(img))
print(img.shape)

for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]



tag = img[20:30, 10:50]
img[0:10, 10:50] = tag
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()