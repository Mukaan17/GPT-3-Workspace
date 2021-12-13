# -*- coding: utf-8 -*-
# @Author: Mukhil Sundararaj
# @Date:   2021-12-03 09:48:19
# @Last Modified by:   Mukhil Sundararaj
# @Last Modified time: 2021-12-13 15:50:37
from genericpath import getsize
import os
from sys import getsizeof
import openai
import speech_recognition as sr
import pyttsx3


openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to
# speech
def SpeakText(command):
	
	# Initialize the engine
	engine = pyttsx3.init()
	# Use male voice	
	voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
	engine.setProperty('voice', voice_id)
	engine.say(command)
	engine.runAndWait()

#Sample rate is how often values are recorded
sample_rate = 24000
#It is advisable to use powers of 2 such as 1024 or 2048
chunk_size = 2048
#Initialize the recognizer
r = sr.Recognizer()

text = ""
while(1):
	#Use the microphone as source for input. Here, we also specify
	#which device ID to specifically look for incase the microphone
	#is not working, an error will pop up saying "device_id undefined"
	with sr.Microphone(device_index = 1, sample_rate = sample_rate,
							chunk_size = chunk_size) as source:
		#Wait for a second to let the recognizer adjust the
		#energy threshold based on the surrounding noise level
		r.adjust_for_ambient_noise(source)
		print ("I'm listening...")
		SpeakText("I'm listening")
		#listens for the user's input
		audio = r.listen(source)
		
		try:
			text += r.recognize_google(audio)
			print (text + "\n")
		
		#Error occurs when google could not understand what was said
		
		except sr.UnknownValueError:
			print("Speech Recognition could not understand audio")
		
		except sr.RequestError as e:
			print("Could not request results from Speech Recognition service; {0}".format(e))


	#GPT-3 API Call
	response = openai.Completion.create(
	engine="davinci-instruct-beta-v3",
	prompt=text,
	temperature=0.7,
	max_tokens=150,
	top_p=1,
	frequency_penalty=0.35,
	presence_penalty=0.64,
	)
	
	#GPT-3 TTS 
	print(response.choices[0].text)
	SpeakText(response.choices[0].text)

	#Conversation memory
	text += response.choices[0].text
	s= getsizeof(text)
	if(s > 150):
		text=""
