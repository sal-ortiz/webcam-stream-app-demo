# import the opencv library
import cv2


def screenshot():
    global vid
    cv2.imwrite('screenshot.png',vid.read()[1])





# define a video capture object
vid = cv2.VideoCapture(0)

while(True):

    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('s'):
        screenshot()

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
