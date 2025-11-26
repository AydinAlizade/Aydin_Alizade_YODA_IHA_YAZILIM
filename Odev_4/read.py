import cv2 as cv

# img = cv.imread('Odev_4/Resources/Photos/cat_large.jpg')

# cv.imshow('Cat', img)

# cv.waitKey(0) # 0 means wait indefinitely until a key is pressed

# Reading Videos

capture = cv.VideoCapture('Odev_4/Resources/Videos/dog.mp4') # Your webcam is 0, external camera is 1

# Start an infinite loop to read the video frame by frame
while True:
    isTrue, frame = capture.read() # capture.read returns two values: a boolean (isTrue) and the current frame
    if not isTrue: # If there are no more frames to read, exit the loop
        break
    cv.imshow('Video', frame) # Display the current video frame

    # Wait 20 milliseconds for a keypress.
    # If the user presses the 'd' key, exit the loop.
    if cv.waitKey(20) & 0xFF == ord('d'): # cv.waitKey(20) stops the program for 20 milliseconds and if the user presses any key during that time, it returns the ASCII value of the key pressed
        break

capture.release() # Release the video file or webcam after finishing
cv.destroyAllWindows() # Close all OpenCV windows