import cv2 as cv
from pathlib import Path

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

parent_dir = Path(__file__).parent


#change resulation of webcam

def changeRes(width, height):
    
    #only work for live video capture
    capture.set(3,width)
    capture.set(4,height)
#image rescale part
img = cv.imread(f'{parent_dir}/assets/photos/img1.jpg')

img = rescaleFrame(img,.2)

cv.imshow('image1', img)
cv.waitKey(0)



#video rescale part
video = cv.VideoCapture(f'{parent_dir}/assets/videos/video1.mp4')

while True:
    isTrue, frame = video.read()
    
    resized_frame = rescaleFrame(frame,.2)
    cv.imshow('video', resized_frame)
    
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
    
video.release()
cv.destroyAllWindows()