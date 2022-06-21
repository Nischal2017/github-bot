import json
import random
import time
import uuid
from datetime import datetime

def generateRandomJson(dateAndTime):
	
	data = {}
	keyF = "key"
	valueF = "value"
	
	for i in range(0,random.randint(3,9)):
		keyF = keyF[:3]+str(uuid.uuid4().hex)
		valueF = valueF[:5]+str(uuid.uuid4().hex)
		data[keyF] = valueF
	
	data["dateAndTime"] = dateAndTime
	return data

def writeIntoFile(fileN , data):
	
	file = open(fileN,'w')
	jsondata = json.dumps(data)
	file.write(jsondata)
	return "Data Written into " + fileN

def makeCommits(day):
	
	file = "commitData.json"
	dateAndTime = datetime.utcfromtimestamp(time.time()+3600*5.5-(86400*day)).strftime('%Y-%m-%d %H:%M:%S')
	data = generateRandomJson(dateAndTime)
	result = writeIntoFile(file,data)
	print(data["dateAndTime"],len(data),result,sep="\n")
	return [data["dateAndTime"],len(data)]



# os.system("git add .")
# os.system('git commit --date="'+d+'" -m commit')
# os.system('git push')