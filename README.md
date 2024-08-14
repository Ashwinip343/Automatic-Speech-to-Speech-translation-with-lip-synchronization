# Automatic-Speech-to-Speech-translation-with-lip-synchronization
 Building an automated pipeline capable of translating a video of a person speaking in language A into a target language B with voice transfer/cloning & realistic lip synchronization, consisting of several pre-trained, open-source deep learning models for enhanced lip synchronized video generation.


The whole pipeline consists of several phases :

- Video preprocessing & extracting audio from the original video - Python Scripts
- Speech transctiption of the extracted audio (Speech to text) - Speech matics API / Wav2Vec2 
- Text translation (Text to text , translating the content of text to another language) - Speech matics
- Text to speech with voice transfer (speech synthesis in the target language with voice cloning) - Tortoise TTS 
- Lip Synchronization - Wav2lip  
-  Enhancing video quality - ESRGAN


<img width="820" alt="ats" src="https://github.com/user-attachments/assets/8e48dfa8-514b-4623-bcd1-993ebd01dc80">
