import os
import datetime
import random
path = 'D:\\'

lists = os.listdir(path)
now = datetime.datetime.now()
id = 0
print (lists)
for dir in lists:
	if 'id' in dir:
		id = dir.split("id")[1]
		for workdir in os.listdir(path+"\\"+str(dir)):
			if "Сделано" in workdir:
				os.chdir(path+"\\"+str(dir)+"\\"+str(workdir))
				for i in range(2,random.randint(2,7)):
					file = open("ID_"+str(id)+"_falcon_"+str(random.randint(531,9999))+"_"+str(now.second)+".tif", "w")
			if "Переделано" in workdir:
				os.chdir(path+"\\"+str(dir)+"\\"+str(workdir))
				for i in range(2,random.randint(2,7)):
					file = open("ID_"+str(id)+"_falcon_"+str(random.randint(531,9999))+"_"+str(now.second)+".tif", "w")
			if "Жду ответа" in workdir:
				os.chdir(path+"\\"+str(dir)+"\\"+str(workdir))
				for i in range(2,random.randint(1,3)):
					file = open("ID_"+str(id)+"_falcon_"+str(random.randint(531,9999))+"_"+str(now.second)+".tif", "w")
