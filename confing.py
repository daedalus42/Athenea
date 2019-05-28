from __future__ import division
import numpy as np
import cv2
import time
import RPi.GPIO as GPIO
import os
import picamera
import picamera.array
import subprocess
import re
import sys
import pyaudio
from pygame import mixer
from six.moves import queue

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import type
from google.cloud import vision

import MicrophoneStream as ms
import SpeechToText as st
import tts_google as tts

from motor import *
from emotion import *
from facialRecognition import *
from sensores import *
from led import  *
from jokes import *

#Google Cloud
credentials= "Robot-a3a386cc00fa.json"

#Pines Motor
mIn1 = 20
mIn2 = 19
mEn= 16  #enabled
mPWM =1000

#Pines Led Red
rIn1 = 27
rIn2 = 22
rEn= 17
rPWM =200

#Pines Led Green
gIn1 = 8
gIn2 = 7
gEn= 25
gPWM =200

#Pines Led Blue
bIn1 = 9
bIn2 = 10
bEn= 11
bPWM =200

#IR
#AD AI OD OI
WR = 26
WL = 19
ER = 13
EL = 6


classifier = '/home/pi/opencv/data/haarcascades/haarcascade_frontalface_default.xml'
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials


