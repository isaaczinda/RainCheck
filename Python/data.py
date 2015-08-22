import subprocess

MatrixData = ""
PointsData = ""

def ConvertToInt(l):
	for x in range(0, len(l)):
		for y in range(0, len(l[0])):
			l[x][y] = int(l[x][y]) 
	return l

def ProcessValues(a):
	FinalList = []
	for i in range(0, len(a)):
		FinalList.append([])
		for q in range(0, len(a[i])):
			Value = a[i][q]

			if Value < 0:
				Value = 0

			
			FinalList[i].append(Value)	
	return FinalList

def MakeTwoDimensional(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]

def FetchData():
	global MatrixData, PointsData


	Data = subprocess.Popen("/home/isaac/Android/Sdk/platform-tools/adb shell \"cat /proc/absolute_position_reporting & cat /proc/test_reporting & wait\"", shell=True, stdout=subprocess.PIPE).stdout.read()

	Array = Data.split("][")



	Array[0] = Array[0].replace("[", "")
	Array[1] = Array[1].replace("]", "")


	#I don't know which string is which, but I know that matrix is always longer
	if len(Array[0]) > len(Array[1]):
		MatrixData = Array[0]
		PointsData = Array[1]
	else:
		MatrixData = Array[1]
		PointsData = Array[0]


def GetData():
	global MatrixData
	Array = MatrixData.split(",")

	#remove last item (it was caused by excess comma)
	del Array[len(Array) - 1]

	return Array

def GetPointsData():
	global PointsData
	Array = PointsData.split(",")

	#remove last item (it was caused by excess comma)
	del Array[len(Array) - 1]

	Array = MakeTwoDimensional(Array, 2)

	return ConvertToInt(Array)

def GetMatrixData():
	Items = GetData()
	TwoDimensional = MakeTwoDimensional(Items, 15)
	IntConverted = ConvertToInt(TwoDimensional)
	return IntConverted
