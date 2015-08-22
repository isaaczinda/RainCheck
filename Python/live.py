import subprocess
import rendering
import json
import sys
import select
import data
import time

def PrintRawValues(List):
	subprocess.Popen("clear", shell=True)
	time.sleep(.05);
	print('\n'.join([''.join(['{:8}'.format(item) for item in row]) for row in List]))

#records until enter is pressed
while True:
	#actually gets all of the data
	data.FetchData()	

	#does some conversions
	Points = data.GetPointsData()
	Matrix = data.GetMatrixData()

	print(Points)	

	# use unusable.Calculate(Matrix) to calculate spots that are wet
	rendering.Update(Matrix, Points, [], [], True)	
	







