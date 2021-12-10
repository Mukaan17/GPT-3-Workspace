# -*- coding: utf-8 -*-
# @Author: Mukhil Sundararaj
# @Date:   2021-12-10 12:01:24
# @Last Modified by:   Mukhil Sundararaj
# @Last Modified time: 2021-12-10 12:03:06
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.runAndWait()
for voice in voices:
    # to get the info. about various voices in our PC 
    print("Voice:")
    print("ID: %s" %voice.id)
    print("Name: %s" %voice.name)
    print("Age: %s" %voice.age)
    print("Gender: %s" %voice.gender)
    print("Languages Known: %s" %voice.languages)