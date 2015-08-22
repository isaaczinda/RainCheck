import rendering
import json
import time
import sys
import os

def PlayClip(Filename):
	print("Playing " + Filename + " with " + str(SleepTime) + "msec frames.")

	File = open("DataFiles/" + Filename, 'r')
	Value = File.read()
	File.close()
	
	Object = json.loads(Value)

	for Frame in range(0, len(Object)):
		StartTime = int(round(time.time() * 1000))
		rendering.Update(Object[Frame]["Matrix"], Object[Frame]["Points"], [], [], True)
		EndTime = int(round(time.time() * 1000))

		TimeRemaining = SleepTime - (EndTime - StartTime)
	
		if TimeRemaining > 0:
			time.sleep(float(TimeRemaining) / 1000.0)

SleepTime = 200

if len(sys.argv) >= 3:
	if sys.argv[2] == "slow":
		SleepTime = 500
	if sys.argv[2] == "medium":
		SleepTime = 200
	if sys.argv[2] == "fast":
		SleepTime = 100

if sys.argv[1] == "all":
	for File in os.listdir("DataFiles"):
		PlayClip(File)	
else:
	PlayClip(sys.argv[1])



	


	







