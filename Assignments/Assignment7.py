import json
import sys
sys.path.append('../Module')
import WulfModule

def OpenFile(filename):
    jsonTxt = ""
    f = open(filename)
    for line in f:
        line = line.strip()
        jsonTxt = jsonTxt + line
    Courses = json.loads(jsonTxt)
    return Courses

def ReadInfo(Courses):
    name = WulfModule.UserString("Enter a course name:")
    for course in Courses:
        print course
        if course["Course Name"] == name:
            print "%s" % course["Course Name"] + " -",
            for professorName in course["Professor Name"]:
                print professorName
            for location in course["Class Location"]:
                print location
            for grade in course["Grade"]:
                print grade
    
def Main():
    ClassList = OpenFile('Classes.json')
    ReadInfo(ClassList)
    

    
    

Main()
