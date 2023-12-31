from streamlit_webrtc import webrtc_streamer
import streamlit as st
import streamlit_lottie as st_lottie
import tensorflow as tf
from apikey import api_key
from langchain.llms import OpenAI
import numpy as np
import os
from video_processing import VideoProcessor
from model_utils import load_model
from utils import load_video

#Basic page configuration
st.set_page_config(
    page_title='SynchAI',
    page_icon='🤖',
)

os.environ['OPENAI_API_KEY']=api_key
llm = OpenAI(temperature=0.9)
st.title('SynchAI')
st.write('Aiding to track precision')

# Setting up the streamer with all the pre-processing done!
start_recording = st.button('Start')
stop_recording = st.button('Stop')


output_file = 'output.mp4'
processor = VideoProcessor(output_file)

class get_video:
    def recv(self,frame):
        return frame
video_streamer=webrtc_streamer(key='Video',video_processor_factory=get_video)

def get_next_frame_from_webrtc_stream(streamer):
    if streamer:
        frame = streamer.video_receiver.get_frame(timeout=10)
        return frame

while start_recording:
    frame = get_next_frame_from_webrtc_stream(video_streamer)
    if frame is not None:
        processor.process_frame(frame)
        processor.finish_processing()

    if stop_recording:
        processor.process_frame(frame)
        processor.finish_processing()
        break

# processor.finish_processing()
def generate_prompt(prompt):
    response = llm(prompt)
    st.info(response)

if st.button('Generate Prompt'):
    generate_prompt(prompt = 'Generate a general interview question for the post of SDE')


    model = load_model()
    yhat = model.predict(tf.expand_dims(output_file, axis=0))
    decoder = tf.keras.backend.ctc_decode(yhat, [75], greedy=True)[0][0].numpy()
    st.text(decoder)

converted_prediction = tf.strings.reduce_join(num_to_char(decoder)).numpy().decode('utf-8')
st.text(converted_prediction)
