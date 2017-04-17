import json
import sys
sys.path.append('../Module')
import WulfModule

def main():
    jsonTxt = ""
    f = open('Exam5.json')
    for line in f:
        line = line.strip()
        jsonTxt = jsonTxt + line
    Courses = json.loads(jsonTxt)
    print Courses
    name = WulfModule.UserString("Enter a Category:")
    for course in Courses:
        if course["Category"] == name:
            print "%s" % course["Product"] + " -", 
            print "%s" % course["Price"]
                
                
                
                
main()