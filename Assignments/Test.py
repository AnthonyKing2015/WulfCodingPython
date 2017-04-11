import json
import sys
sys.path.append('../Module')
import WulfModule

def main():
    jsonTxt = ""
    f = open('Classes.json')
    for line in f:
        line = line.strip()
        jsonTxt = jsonTxt + line
    Courses = json.loads(jsonTxt)

    name = WulfModule.UserString("Enter a course name:")
    for course in Courses:
        if course["Course Name"] == name:
            print "%s" % course["Course Name"]
            for professorName in course["Professor Name"]:
                print professorName
            for location in course["Class Location"]:
                print location
            for grade in course["Grade"]:
                print grade
                
                
                
                
main()