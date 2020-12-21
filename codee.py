# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 19:16:58 2020

@author: vijay
"""

## By: Vijay Chadokar & Atharva Mishra
import concurrent.futures
import time
import pandas
import pyaudio
from Exam import questn_win
from datetime import datetime
from saver import sus_audio_saver,sus_video_saver,cv2
from array import array
import Authorize
from Authorize import authorize

start = time.perf_counter()
stop = True
record_1 = pandas.DataFrame(columns=["Movements"])
record_2 = pandas.DataFrame(columns=["Noises"])


def audio_recorder():
    global stop, record_2
    FORMAT = pyaudio.paInt16
    RATE = 11025  # 44100
    CHUNK = 1024
    

    audio = pyaudio.PyAudio()

    stream = audio.open(format=FORMAT, channels=1,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)
    frames = []
    times = []

    while stop:
        for i in range(0, int(RATE / CHUNK)):
            data = stream.read(CHUNK)
            data_chunk = array('h', data)
            vol = max(data_chunk)
            if (vol >= 700):
                print("Noise detected\n\n")
                frames.append(data)
                times.append(datetime.now().time())
            else:
               print("No Noise")
               print("\n")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    sus_audio_saver(frames,audio.get_sample_size(FORMAT))
    for i in range(0, len(times), 1):
        record_2 = record_2.append({"Noises": times[i]}, ignore_index=True)

def video_recorder():
    global stop, record_1
    can_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


    times=[]
    refframe = None
    invigilator = cv2.VideoCapture(0)
    pre = 0
    sus_frames=[]
    get_verified=False
    
    img_orig=cv2.imread("known.png",1)
    win_candidate='Candidate' 
    img_orig=cv2.resize(img_orig,(137,155),interpolation = cv2.INTER_AREA)
    cv2.imshow(win_candidate, img_orig)
    cv2.moveWindow(win_candidate,15,15)
    
    while True:
    
        boval,frame = invigilator.read()
        flag = 0
        grayi = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        candidate = can_cascade.detectMultiScale(grayi, scaleFactor=1.05, minNeighbors=5)
        flag = len(candidate)
        if (flag == 0):
            times.append(datetime.now())
            cv2.putText(frame, 'Candidate not detectable !!!', (50, 100), cv2.FONT_HERSHEY_COMPLEX, 0.75, (0, 0, 255), 2)
            get_verified=False
        if get_verified==False:
            ret_code=authorize(frame)
            print('\nget_verified\n')
            print(ret_code)
            sus_frames.append([frame,datetime.now().strftime("%Y%m%d-%H%M%S")])
            if ret_code=='Matched':
                get_verified=True
        gr = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gr = cv2.GaussianBlur(gr, (21, 21), 0)
        if refframe is None:
            refframe = gr
            continue
        difff = cv2.absdiff(refframe, gr)
        thf = cv2.threshold(difff, 30, 255, cv2.THRESH_BINARY)[1]
        thf = cv2.dilate(thf, None, iterations=0)
        (_,cnts, _) = cv2.findContours(thf.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        val = 1
        for contour in cnts:
            if cv2.contourArea(contour) > 2000:
                val += 1
            if cv2.contourArea(contour)> 3500:
                (x,y,w,h)=cv2.boundingRect(contour)
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255))
                sus_frames.append([frame,datetime.now().strftime("%Y%m%d-%H%M%S")])
                if val>2:
                    continue
        if val >= 3:
            pre = pre + 1
        else:
            pre = 0
        if (pre > 10 and pre < 30):
            times.append(datetime.now().time())
            cv2.putText(frame, 'Warning:Please sit steady facing the webcam !!!', (20, 30), cv2.FONT_HERSHEY_COMPLEX, 0.75, (0, 0, 255), 2)
            for x,y,w,h in candidate:
                frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
            sus_frames.append([frame,datetime.now().strftime("%Y%m%d-%H%M%S")])
        if (pre > 32):
            refframe = gr
        win_name='Virtual invigilator'
        cv2.moveWindow(win_name,920,390)
        frame=cv2.resize(frame,(390,280),interpolation = cv2.INTER_AREA)
        cv2.imshow(win_name, frame)
    
        k = cv2.waitKey(2)
        if k == ord('q'):
            stop=False  
            break
    
    invigilator.release()
    cv2.destroyAllWindows()    

        
    sus_video_saver(sus_frames)
    for i in range(0, len(times), 1):
        record_1 = record_1.append({"Movements": times[i]}, ignore_index=True)
        
        


f1 = concurrent.futures.ThreadPoolExecutor().submit(questn_win)
f2 = concurrent.futures.ThreadPoolExecutor().submit(video_recorder)
f3 = concurrent.futures.ThreadPoolExecutor().submit(audio_recorder)

#
f1.result()
f2.result()
f3.result()
#

df_final=pandas.concat([record_1,record_2],axis=1) 
df_final.to_csv("Suspicious.csv")
finish = time.perf_counter()

print('Completed in ', finish - start, ' seconds')

