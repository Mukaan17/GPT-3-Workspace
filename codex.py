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


"""
A program to use GPT-3 Completion with speech as input

"""











































































