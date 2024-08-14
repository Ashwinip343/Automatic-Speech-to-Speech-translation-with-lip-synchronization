# Automatic-Speech-to-Speech-translation-with-lip-synchronization
The Project proposes the development of an automated pipeline capable of translating a video of a person speaking in language A into a target language B with voice transfer/cloning & realistic lip synchronization, consisting of several pre-trained, open-source deep learning models for enhanced lip synchronized video generation.

The convergence of artificial intelligence and multimedia technologies has paved the way for innovative solutions in the domain of speech-to-speech translation. Traditional approaches often fall short in capturing the nuances of natural speech and maintaining lip synchronization, leading to poor user experiences. This project aims to overcome these limitations by incorporating deep learning architectures and techniques to create a robust and efficient translation pipeline. By integrating audio and visual modalities , we aim to build an automated pipeline to achieve accurate lip synchronized video.

The whole pipeline consists of several phases :

- Video preprocessing & extracting audio from the original video - Python Scripts
- Speech transctiption of the extracted audio (Speech to text) - Speech matics API / Wav2Vec2 
- Text translation (Text to text , translating the content of text to another language) - Speech matics
- Text to speech with voice transfer (speech synthesis in the target language with voice cloning) - Tortoise TTS 
- Lip Synchronization - Wav2lip  
-  Enhancing video quality - ESRGAN


<img width="820" alt="ats" src="https://github.com/user-attachments/assets/8e48dfa8-514b-4623-bcd1-993ebd01dc80">
