<h1>SynchAI</h1>

<h2>What is it about?</h2>
<p>
This is a web-based CV platform that is capable of tracking eye movement, generating captions and the through ML-Aided lip-synch, figure out whether the answers are appropriate.
</p>

<h2>How it shall be built?</h2>
<p>
The app shall be based on the following technologies- 
<ol>
  <li><b>Streamlit in python for the web interface</b>: - a python package that shall cater to scalable,online application needs</li>
  <li><b>MediaPipe by google</b>: For functionalities of eye-tracking, and face mesh</li>
  <li><b>Tensorflow</b>: This is to build from scratch the very system of lip-synching </li>
</ol>
</p>

<h2>The web interface</h2>
<p>
  The web-interface for the app is made using streamlit, which is to ensure a light-weight front-end for an already intensive back-end.<br>
  The app shall be a dual page,simple yet intelligent app that wouldd boast a live cameera-input layered with our ML implementations to ensure functionalities of eye-        
   tracking,and lip-synch to monitor Q/Ans prcess<br>
  ![image](https://github.com/VishwakarmaIntelligentSystems/SynchAI/assets/141939916/78c98da4-af2e-40e5-872c-64e18b9d28b4)



  As the stream is started, tt shal open up the video stream live from the camera and implement al the ffunctionalities on top of it.<br>
  Before this happens, the user/admnistrator can also make the camera and audio adjustments as well throughh the "select device" option.<br>
  ![image](https://github.com/VishwakarmaIntelligentSystems/SynchAI/assets/141939916/ce01aa89-4b59-4cff-a298-0bf035a1ba14)

It also has been currently equipped witrh a temporary functionality to be able to generate prompts by itself for interviews that can be tweaked and is a broad part of the whole app functionality which includes tracking lip movement according to the prompt generated
![image](https://github.com/id1ne/id1ne_repo/assets/141939916/a8ae9596-79d7-4e58-9e3f-6252f11080da)
It uses the OpenAI API for the same
![image](https://github.com/id1ne/id1ne_repo/assets/141939916/07f31c87-21cb-4533-95d6-44a84f9a9d0d)
And harnessing the power of LLMs, it is able to generate new prompts/questions everytime!
![image](https://github.com/id1ne/id1ne_repo/assets/141939916/1ab96139-9fae-49a1-b7f1-bf3b51139d46)
</p>

<h2>The Machine learning</h2><br>
<h3>Lip-Reading</h3>
<p>
SynchAi shall rely on lip-synching to be able to generate speech transcriptions without the use of audio.
This shall be a custom model built from scratch that shall be trained on videos and their existing transcription alignments - explicitly tracking lip movement.
Some images from the model training processes-<br>
![image](https://github.com/VishwakarmaIntelligentSystems/SynchAI/assets/141939916/20192c20-832b-49ca-826a-a3aa001c2d38)<br>
![image](https://github.com/VishwakarmaIntelligentSystems/SynchAI/assets/141939916/2daa29d0-63e4-4bcb-b88d-4c123aa75f6c)<br>
![image](https://github.com/VishwakarmaIntelligentSystems/SynchAI/assets/141939916/21fd243c-6f6e-4f5f-a49f-97c5b2a89f9a)<br>
![image](https://github.com/VishwakarmaIntelligentSystems/SynchAI/assets/141939916/ad14f312-af60-40d8-a746-67e2d633659a)<br>

The SynchAI lip-tracking model can select the lip-region and based on the movement and trained transcriptions- can give fairly accurate account of what is being spoken
(as can be observed by the gradual movement)<br>

![animation](https://github.com/VishwakarmaIntelligentSystems/SynchAI/assets/141939916/ddc4fbd7-6eb1-4ad8-8f17-21426ac6e32d)

</p>
