import os
FileName = []
files = os.listdir(".")
d = {}
for item in files: 
        if ".txt" in item:
            FileName.append(item)
for i in range(0,2):
   d[FileName[i]] = []

f = open()
for line in f: 
    temp = line.strip('')
    
