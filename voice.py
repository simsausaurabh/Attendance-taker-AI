# Import the required module for text 
# to speech conversion
from gtts import gTTS
import vlc
import time
import speech_recognition as sr
import datetime

# This module is imported so that we can 
# play the converted audio
import os

# For creating roll nos audios from start uncomment below code
# i=0
# file = open("student.txt", "r")

# for rollNo in file:


# 	mytext = rollNo

# 	# Language in which you want to convert
# 	language = 'en'
	 
# 	# Passing the text and language to the engine, 
# 	# here we have marked slow=False. Which tells 
# 	# the module that the converted audio should 
# 	# have a high speed
# 	myobj = gTTS(text=mytext, lang=language, slow=True)
# 	if i<63:
# 		myobj.save("rollno" + str(i) + ".mp3")
# 		i = i+1


outputFile = open("output.txt", "w")

outputFile.write("Attendance for: " + str(datetime.datetime.now()) + "\n")

# Set the range based on the no of students(or roll numbers)
for v in range(0, 5):
	
	# Playing the converted file
	os.system("mpg321 rollno"+str(v)+".mp3")
	r = sr.Recognizer()

	with sr.Microphone() as source:
		print "Please wait. Calibrating microphone..."
		# listen for 1 second and create the ambient noise energy level
		r.adjust_for_ambient_noise(source, duration=2)
		print "Say something!"
		
		audio = r.listen(source, phrase_time_limit=5)

	try:
		responseObject = r.recognize_google(audio)
		response = str(responseObject)
		present1 = "yes"
		present2 = "present"

		print "response: "
		print response

		# outputFile.write(str(v) + " absent\n")
		if (response==present1) or (response==present2):
			outputFile.write(str(v) + "  PRESENT\n")
		else:
			outputFile.write(str(v) + "  ABSENT\n")
	except sr.UnknownValueError:
		print "Google Speech Recognition could not understand audio"
	except sr.RequestError as e:
		print "Could not request results from Google Speech Recognition service"

outputFile.write("\n")
outputFile.close()
