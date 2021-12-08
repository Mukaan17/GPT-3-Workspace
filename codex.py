# -*- coding: utf-8 -*-
# @Author: Mukhil Sundararaj
# @Date:   2021-12-08 15:24:12
# @Last Modified by:   Mukhil Sundararaj
# @Last Modified time: 2021-12-08 15:37:35
"""
A program to print 'hello world'

""" 
print("hello world")

"""
A program to implement speech recognition

"""
import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize what you said")












































































