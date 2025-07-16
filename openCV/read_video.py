import cv2 as cv
from pathlib import Path

parent_dir = Path(__file__).parent

# capture = cv.VideoCapture(0)
video = cv.VideoCapture(f'{parent_dir}/assets/videos/video1.mp4')

while True:
    # isTrue, frame = capture.read()
    isTrue, frame = video.read()
    cv.imshow('webcam', frame)
    
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
video.release()
cv.destroyAllWindows()