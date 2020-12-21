# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 19:24:28 2020

@author: vijay
"""
import wave
import cv2 
def sus_audio_saver(frames,sample_size):
    RATE = 11025  # 44100
    wavfile = wave.open("Noises.wav", 'wb')
    wavfile.setnchannels(1)
    wavfile.setsampwidth(sample_size)
    wavfile.setframerate(RATE)
    wavfile.writeframes(b''.join(frames))
    wavfile.close()
   
def sus_video_saver(frames_with_time):
    for frame in frames_with_time:
        cv2.imwrite(frame[1]+'.jpg',frame[0])
   