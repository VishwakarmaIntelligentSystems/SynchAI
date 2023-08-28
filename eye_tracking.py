import mediapipe as mp
import cv2

mp_face = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

input = cv2.VideoCapture(0)
while input.isOpened():
    ret,frame = input.read()
    img = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    annotations = mp_face.FaceMesh(refine_landmarks=True).process(img)
    img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
    if annotations.multi_face_landmarks:
        for landmarks in annotations.multi_face_landmarks:
            mp_drawing.draw_landmarks(
                image=img,
                landmark_list=landmarks,
                connections=mp_face.FACEMESH_NUM_LANDMARKS_WITH_IRISES,
                landmark_drawing_spec=None,
                connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_iris_connections_style()

            )
            mp_drawing.draw_landmarks(
                image=img,
                landmark_list=landmarks,
                connections=mp_face.FACEMESH_TESSELATION,
                landmark_drawing_spec=None,
                connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_tesselation_style()
            )
    cv2.imshow('Eye tracking',img)
    if cv2.waitKey(0) & 0xFF==ord('q'):
        break

input.release()
cv2.destroyAllWindows()


