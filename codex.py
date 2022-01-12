# -*- coding: utf-8 -*-
# @Author: Mukhil Sundararaj
# @Date:   2021-12-13 16:06:06
# @Last Modified by:   Mukhil Sundararaj
# @Last Modified time: 2022-01-12 18:30:01
import openai
import pyttsx3
import speech_recognition as sr
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

	with sr.Microphone(device_index = 1, sample_rate = sample_rate,chunk_size = chunk_size) as source:
		r.adjust_for_ambient_noise(source)
		print ("\n Please provide your problem statement:")
		SpeakText("Please provide your problem statement")
		audio = r.listen(source)
		
		try:
			text = r.recognize_google(audio)
			print (text + "\n")
		
		except sr.UnknownValueError:
			print("Speech Recognition could not understand audio")
		
		except sr.RequestError as e:
			print("Could not request results from Speech Recognition service; {0}".format(e))


	#GPT-3 API Call
	response = openai.Completion.create(
        engine="davinci-codex",
        prompt=text,
        temperature=0.35,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
	
	#GPT-3 TTS 
	print(response.choices[0].text)