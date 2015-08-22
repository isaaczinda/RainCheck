import rendering
import json
import sys
import select
import data

VideoArray = []

def Enter():
	i, o, e = select.select( [sys.stdin], [], [], .001)

	if (i):
		return True
	else:
		return False

Filename = sys.argv[1]

print("Saving data to " + Filename)

print("Press enter to end recording.") 

#records until enter is pressed
while Enter() == False:
	#actually gets all of the data
	data.FetchData()	

	#does some conversions
	Points = data.GetPointsData()
	Matrix = data.GetMatrixData()	

	print(Points)

	VideoArray.append({"Matrix": Matrix, "Points": Points})	
raw_input()



FileValue = json.dumps(VideoArray)

File = open("DataFiles/" + Filename, 'w')
File.write(FileValue)
File.close()

print("Wrote " + str(len(FileValue)) + " bytes to " + Filename)
	







