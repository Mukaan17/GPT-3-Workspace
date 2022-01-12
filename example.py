# -*- coding: utf-8 -*-
# @Author: Mukhil Sundararaj
# @Date:   2021-12-03 09:48:19
# @Last Modified by:   Mukhil Sundararaj
# @Last Modified time: 2022-01-12 18:13:36
from genericpath import getsize
from sys import getsizeof
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
		print ("Ask me anything...")
		SpeakText("Ask me anything")
		audio = r.listen(source)
		
		try:
			text += r.recognize_google(audio)
			print (text + "\n")
		
		except sr.UnknownValueError:
			print("Speech Recognition could not understand audio")
			text = "Tell me you couldn't hear me"
		
		except sr.RequestError as e:
			print("Could not request results from Speech Recognition service; {0}".format(e))
			text = "Tell me you couldn't hear me"


	#GPT-3 API Call
	response = openai.Completion.create(
	engine="davinci-instruct-beta-v3",
	prompt=text,
	temperature=0.7,
	max_tokens=1024,
	top_p=1,
	frequency_penalty=0.35,
	presence_penalty=0.64,
	)
	
	#GPT-3 TTS 
	SpeechT = response.choices[0].text.split("\n\n")
	print(SpeechT[1])
	SpeakText(SpeechT[1])