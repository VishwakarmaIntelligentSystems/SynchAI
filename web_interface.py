import mediapipe as mp
import numpy as np
import av

facemesh = mp.solutions.face_mesh
face = facemesh.FaceMesh(static_image_mode=True,min_detection_confidence=0.5,min_tracking_confidence=0.6)
draw = mp.solutions.drawing_utils

st.title('SynchAI')
st.write('Aiding to track precision')

class video_processing:
    def recieve_video(self,frame):
        frm = frame.to_ndarray(format='bgr24')
        rgb = frame.to_ndarray(format='rgb24')
        output = face.process(rgb)
        if output.multi_face_landmarks:
            for landmarks in output.multi_face_landmarks:
                print(landmarks)
                draw.draw_landmarks(rgb,landmarks)
        return av.VideoFrame.from_ndaray(frm,format='bgr24')

webrtc_streamer(key='video',video_processor_factory=video_processing)
