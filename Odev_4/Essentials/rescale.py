import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    # Works for images, videos and live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    # works for live video only
    capture.set(3, width)
    capture.set(4, height)  

capture = cv.VideoCapture('Odev_4/Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    if not isTrue:
        break
    frame_resized = rescaleFrame(frame, 0.20)  
    cv.imshow('Video', frame)
    cv.imshow('Resized Video', frame_resized)   

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()