import sys
sys.path.append('../Module')
import WulfModule
import os


def AskUserForWord():
    l = WulfModule.UserString("Please enter a search term:")
    LUpper = l.upper()
    return LUpper

    
def ReadInfile(l):
    d = {}
    NewFileList = []
    files = os.listdir(".")
    for item in files: 
        if ".txt" in item:
            NewFileList.append(item)
    for item in NewFileList:
        d[item]= []
    for item in NewFileList:
        tempList = []
        for line in open(item):
            line = line.upper().strip()
            tempList.append(line)
        d[item] = tempList
    return d
        
def SearchForWord(l, d):
    count = 0
    results = []
    for item in d:
        for line in d[item]:
            if l in line: 
                count += 1
                results.append(item + ": " + line)
    print "I found %s results" %count
    for i in results:
        print i


def Main():
    word = AskUserForWord()
    print word
    texts = ReadInfile(word)
    SearchForWord(word, texts)
    
Main()
    