import rendering
import json
import time
import sys
import os

def PlayFrame(Filename, TargetFrame):
	File = open("DataFiles/" + Filename, 'r')
	Value = File.read()
	File.close()
	
	Object = json.loads(Value)

	print(len(Object))
	print(TargetFrame)

	if TargetFrame < len(Object):
		print ("Viewing frame " + str(TargetFrame) + " from " + Filename) 
			
		print(Object[TargetFrame]["Matrix"])

		rendering.Update(Object[TargetFrame]["Matrix"], Object[TargetFrame]["Points"], [], [], False)
		rendering.Update(Object[TargetFrame]["Matrix"], Object[TargetFrame]["Points"], [], [], False)
		time.sleep(100)
	else:
		print ("Frame out of range.")


Filename = sys.argv[1]
Frame = sys.argv[2]


PlayFrame(Filename, int(Frame))



	


	







