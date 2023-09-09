import av
import cv2
import streamlit as st

face_cascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascades/haarcascade_eye.xml")

class VideoProcessor:
    def __init__(self, output_file):
        self.output_file = output_file
        self.output = av.open(self.output_file, 'w')

    def process_frame(self, frame):
        frm = frame.to_ndarray(format="bgr24")
        faces = face_cascade.detectMultiScale(cv2.cvtColor(frm, cv2.COLOR_BGR2GRAY), 1.1, 3)
        eyes = eye_cascade.detectMultiScale(cv2.cvtColor(frm,cv2.COLOR_BGR2GRAY),1.1,3)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(frm, (ex, ey), (ex + ew, ey + eh), (255, 5, 26), 2)
        for x,y,w,h in faces:
            cv2.rectangle(frm, (x,y), (x+w, y+h), (0,255,0), 3)

        processed_frame = av.VideoFrame.from_ndarray(frm, format='bgr24')

		# Save the processed frame to the output video file
        self.output.mux(processed_frame)

    def finish_processing(self):
        # Close the output file
        self.output.close()

# Instantiating the class and specifying the video file name->
output_file = 'output.mp4'  # Specify the output video file
processor = VideoProcessor(output_file)

