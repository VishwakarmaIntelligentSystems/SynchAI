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
