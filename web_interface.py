import json
import cv2
from streamlit_webrtc import webrtc_streamer
import streamlit as st
import streamlit_lottie as st_lottie
# import tensorflow as tf
import mediapipe as mp
from apikey import api_key
from langchain.llms import OpenAI
from langchain.chains import SimpleSequentialChain,LLMChain
from langchain.prompts import PromptTemplate
import numpy as np
import av
import os

st.set_page_config(
    page_title='SynchAI',
    page_icon='🤖',
)

facemesh = mp.solutions.face_mesh
face = facemesh.FaceMesh(static_image_mode=True,min_detection_confidence=0.5,min_tracking_confidence=0.6)
draw = mp.solutions.drawing_utils

os.environ['OPENAI_API_KEY']=api_key
llm = OpenAI(temperature=0.9)
st.title('SynchAI')
st.write('Aiding to track precision')

class video_processing:
    def process_video(self,frame):
        rgb = frame.to_ndarray(format='rgb24')
        output = face.process(rgb)
        if output.multi_face_landmarks:
            for i in output.multi_face_landmarks:
                draw.draw_landmarks(rgb,i)
        return av.VideoFrame.from_ndarray(rgb)
webrtc_streamer(key='video',video_processor_factory=video_processing)

def generate_prompt(prompt):
    response = llm(prompt)
    st.info(response)

if st.button('Generate Prompt'):
    generate_prompt(prompt = 'Generate a general interview question for the post of SDE')


