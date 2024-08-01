
import cv2


class Camera(object):

    def __init__(self, dev_id=0):
        self.video = cv2.VideoCapture(dev_id)

    def __del__(self):
        self.video.release()

    def take_snapshot(self, filename):
        data = self.video.read()
        cv2.imwrite(filename, data[1])

    def read_stream(self):
        while True:
            frame = self.__get_frame()
            yield frame

    def __get_frame(self):
        success, image = self.video.read()
        ret, jpeg = cv2.imencode('.jpg', image)

        return jpeg.tobytes()