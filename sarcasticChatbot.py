# -*- coding: utf-8 -*-
# @Author: Mukhil Sundararaj
# @Date:   2021-12-28 11:48:40
# @Last Modified by:   Mukhil Sundararaj
# @Last Modified time: 2022-01-12 18:17:12
import os
import openai
import speech_recognition as sr
import pyttsx3
import cred
import config

openai.api_key = cred.OPENAI_API_KEY

# Function to convert text to speech
def SpeakText(command):
	
	# Initialize the engine
	engine = pyttsx3.init()
	voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
	engine.setProperty('voice', voice_id)
	engine.say(command)
	engine.runAndWait()

sample_rate = config.sampleRate
chunk_size = config.chunkSize
r = sr.Recognizer()


while(1):
	text = ""

	with sr.Microphone(device_index = 1, sample_rate = sample_rate,chunk_size = chunk_size) as source:
		r.adjust_for_ambient_noise(source)
		print ("What do you want?\n")
		SpeakText("What do you want?")
		audio = r.listen(source)
		
		try:
			text += r.recognize_google(audio)
			print (text)
		
		except sr.UnknownValueError:
			print("Speech Recognition could not understand audio")
		
		except sr.RequestError as e:
			print("Could not request results from Speech Recognition service; {0}".format(e))


	start_sequence = "You:"
	response = openai.Completion.create(
        engine="davinci-codex", 
        prompt="Marv is a chatbot that reluctantly answers questions.\nYou:"+ text + "? \n",
        temperature=0.3,
        max_tokens=30,
        top_p=0.3,
        frequency_penalty=0.5,
        presence_penalty=0,
        stop=["\n\n"]
    )
	SpeechT = response.choices[0].text.split("\n")
	print("\n" + SpeechT[0])
	Speech = SpeechT[0].split(":")
	SpeakText(Speech[1])