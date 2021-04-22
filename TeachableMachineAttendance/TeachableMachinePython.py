# Import the following in to PyCharm:
#   Pillow
#   Pillow-PIL
#   OpenCV (cv2)

import cv2
import sys
from time import sleep
import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np

class TeachableMachinePython:

    def __init__(self, keras_model, labels_fname):
        self.keras_model = keras_model
        self.labels_fname = labels_fname
        self.labels = []
        self.load_labels()
        self.predicted_label = ""

        # Setup AI Model
        # Disable scientific notation for clarity
        np.set_printoptions(suppress=True)
        # Load the model
        self.model = tensorflow.keras.models.load_model(self.keras_model)
        # Create the array of the right shape to feed into the keras model
        # The 'length' or number of images you can put into the array is
        # determined by the first position in the shape tuple, in this case 1.
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        # Setup Video Capture
        self.video_capture = cv2.VideoCapture(0)

    def load_labels(self):
        my_file = open(self.labels_fname, "r")
        for rec in my_file:
            self.labels.append(rec[2:len(rec) - 1])
        print("Labels are :")
        print(self.labels)

    # using the labels table print highest predicted value
    def show_prediction(self, predict):
        pred_idx = -1.0
        pred_value = -1.0
        for i in range(len(predict)-1):
            if predict[i] > pred_value:
                pred_value = predict[i]
                pred_idx = i
        #self.predicted_label = "%s %2.2f" % (self.labels[pred_idx], pred_value)
        self.predicted_label = "%s" % (self.labels[pred_idx])
        return self.predicted_label

    def display_prediction_on_image(self, frame, predict):
        # Resize frame to be displayed
        scale_percent = 60  # percent of original size
        width = int(frame.shape[1] * scale_percent / 100)
        height = int(frame.shape[0] * scale_percent / 100)
        dim = (width, height)
        frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
        frame = cv2.flip(frame, 1)  # flip horizontally

        predict_text = self.show_prediction(predict)

        # font
        font = cv2.FONT_HERSHEY_SIMPLEX
        # org
        org = (int(width*0.1), int(height*0.95))
        # fontScale
        fontScale = 1
        # Red color in BGR
        color = (1,350,0)
        # Line thickness of 2 px
        thickness = 3
        # Using cv2.putText() method
        frame = cv2.putText(frame, predict_text, org, font, fontScale,
                     color, thickness, cv2.LINE_AA, False)
        return frame

    # call this 4 methods if you wish to access the predicted label of the image.  Call in the order listed
    def main_processing_begin_loop(self):
        if not self.video_capture.isOpened():
            print('Unable to load camera.')
            sleep(5)
            pass

        # Capture frame-by-frame
        frame: object
        ret, frame = self.video_capture.read()

        # Resize the frame to the size of the trained data frame size
        width = 224
        height = 224
        dim = (width, height)
        image = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

        # Do the prediction based on captured frame
        image_array = np.asarray(image)
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        self.data[0] = normalized_image_array
        prediction = self.model.predict(self.data)

        # Display the resulting frame, resize the display image
        frame = self.display_prediction_on_image(frame, prediction[0])
        cv2.imshow('Video', frame)

    def main_check_to_end_loop(self):
        exit_flag = True

        # if you press "q" it will quit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            exit_flag = False

        return exit_flag

    def get_predicted_label(self):
        return self.predicted_label

    def main_loop_stop(self):
        self.video_capture.release()
        cv2.destroyAllWindows()

    # main processing loop without access to predicted label
    def main_processing_loop(self):

        loop_flag = True
        while loop_flag:
            self.main_processing_begin_loop()

            loop_flag = self.main_check_to_end_loop()

        self.main_loop_stop()

# main processing code
'''
my_test = TeachableMachinePython("keras_model.h5", "labels.txt")
#my_test.main_processing_loop()

loop_flag = True
while loop_flag:
    my_test.main_processing_begin_loop()

    print(my_test.get_predicted_label())

    loop_flag = my_test.main_check_to_end_loop()

my_test.main_loop_stop()

'''

print("Done")


