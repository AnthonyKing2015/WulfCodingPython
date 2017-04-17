import json
import sys
sys.path.append('../Module')
import WulfModule

def OpenFile(filename):
    jsonTxt = ""
    f = open(filename)
    for line in f:
        line = line.upper().strip()
        jsonTxt = jsonTxt + line
    PetShop = json.loads(jsonTxt)
    print PetShop
    return PetShop
    
def FindInfo(PetShop):
    Answer = WulfModule.UserString("Search by Category (c) or Keyword (k)?")
    UpperAns = Answer.upper()
    if UpperAns == "C":
        Search = WulfModule.UserString("Please enter a category:")
        SearchCat = Search.upper()
        for category in PetShop:
            if category["CATEGORY"] == SearchCat:
                print "%s" % category["PRODUCT"] + " -", 
                print "$%s" % category["PRICE"]
    if UpperAns == "K":
        Search = WulfModule.UserString("Please enter a Keyword:")
        SearchKey = Search.upper()
        for product in PetShop:
            if SearchKey in product["PRODUCT"]:
                print "%s" % product["PRODUCT"] + " -", 
                print "$%s" % product["PRICE"]
                    
def Main():
    List = OpenFile('Exam5.json')
    FindInfo(List)
                    
Main()
    
    