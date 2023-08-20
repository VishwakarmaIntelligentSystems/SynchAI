import os
import cv2
import tensorflow as tf
import numpy as np
from typing import List
from matplotlib import pyplot as plt
import imageio
import gdown
print("All packages imported")

# For limiting memory growth if running on a GPU
physical_devices = tf.config.list_physical_devices('GPU')
try:
    tf.config.experimental.set_memory_growth(physical_devices[0],True)
except:
    pass

# Downloading training data from google drive
if not os.path.exists('data.zip'):
    url = 'https://drive.google.com/uc?id=1YlvpDLix3S-U8fd-gqRwPcWXAXm8JwjL'
    output = 'data.zip'
    gdown.download(url, output, quiet=False)
    gdown.extractall(output)
else:
    print("The data has already been downloaded")

# The data loading function
def load_video(path:str)->List[float]:
  cap = cv2.VideoCapture(path)
  frames=[]
  for _ in range(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))):
    ret,frame = cap.read()
    frame = tf.image.rgb_to_greyscale(frame)
    frames.append(frame[190:236,80:220,:]) #Isolating the mouth region using a static slicer
  cap.release()

  mean = tf.math.reduce_mean(frames)
  std = tf.math.reduce_std(tf.cast(frames,tf.float32))
  return tf.cast((frames-mean),tf.float32)/std

# Specifying the range of vocabulary we might encounter in our training data
vocab = [x for x in "abcdefghijklmnopqrstuvwxyz'?123456789"]
char_to_num = tf.keras.layers.StringLookup(vocanulary = vocab,oov_token="")
num_to_char = tf.keras.layers.StringLookup(vocabulary = char_to_num.get_vocabulary(),oov_taken = "", invert=True)
print(
    f"The vocabulary is {char_to_num.get_vocabulary()}"
    f"(size = {char_to_num.get_vocabulary_size()})"
)

# Function to load our alignments-
def load_alignments(path:str)->List[str]:
  with open(path,'r') as f:
    lines = f.readlines()
  tokens=[]
  for line in lines:
    line = line.split()
    if line[2] !='sil':
      tokens = [*tokens,' ',line[2]]
  return char_to_num(tf.reshape(tf.strings.unicode.split(tokens,input_encoding = 'UTF-8')))

# This function strives to collectively load videos and the correspondding alignments simeeltaneusly
def load_data(path:str):
  path = bytes.decode(path.numpy())
  file_name = path.split('\\')[-1].split('.')[0]
  video_path = os.path.join('data','s1',f'{file_name}.mpg')
  alignment_path = os.path.join('data','alignments','s1',f'{file_name}.align')
  frames = load_video(video_path)
  alignments = load_alignments(alignment_path)

  return frames,alignments

