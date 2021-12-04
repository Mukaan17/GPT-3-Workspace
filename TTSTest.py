# -*- coding: utf-8 -*-
# @Author: Mukhil Sundararaj
# @Date:   2021-12-03 11:10:50
# @Last Modified by:   Mukhil Sundararaj
# @Last Modified time: 2021-12-03 12:51:54
# Python program to translate
# speech to text and text to speech

'''
import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to
# speech
def SpeakText(command):
	
	# Initialize the engine
	engine = pyttsx3.init()
	engine.say(command)
	engine.runAndWait()
	
	
# Loop infinitely for user to
# speak

while(1):	
	
	# Exception handling to handle
	# exceptions at the runtime
	try:
		
		# use the microphone as source for input.
		with sr.Microphone() as source2:
			
			# wait for a second to let the recognizer
			# adjust the energy threshold based on
			# the surrounding noise level
			r.adjust_for_ambient_noise(source2, duration=0.2)
			
			#listens for the user's input
			audio2 = r.listen(source2)
			
			# Using ggogle to recognize audio
			MyText = r.recognize_google(audio2)
			MyText = MyText.lower()

			print("Did you say "+MyText)
			SpeakText(MyText)
			
	except sr.RequestError as e:
		print("Could not request results; {0}".format(e))
		
	except sr.UnknownValueError:
		print("unknown error occured")
'''


import speech_recognition as sr

#Sample rate is how often values are recorded
sample_rate = 24000
#it is advisable to use powers of 2 such as 1024 or 2048
chunk_size = 2048
#Initialize the recognizer
r = sr.Recognizer()

#use the microphone as source for input. Here, we also specify
#which device ID to specifically look for incase the microphone
#is not working, an error will pop up saying "device_id undefined"
with sr.Microphone(device_index = 1, sample_rate = sample_rate,
						chunk_size = chunk_size) as source:
	#wait for a second to let the recognizer adjust the
	#energy threshold based on the surrounding noise level
	r.adjust_for_ambient_noise(source)
	print ("Say Something")
	#listens for the user's input
	audio = r.listen(source)
		
	try:
		text = r.recognize_google(audio)
		print ("you said: " + text)
	
	#error occurs when google could not understand what was said
	
	except sr.UnknownValueError:
		print("Google Speech Recognition could not understand audio")
	
	except sr.RequestError as e:
		print("Could not request results from Google Speech Recognition service; {0}".format(e))

