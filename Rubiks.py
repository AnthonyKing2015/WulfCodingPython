#import sys
#sys.path.append('../Module')
#import WulfModule

#-------------------------------
# Reads the file and puts the 
# time and names into a dictionary
#---------------------------------
def countTime(filename):
    d = {}
    for line in open(filename):
        temp = line.split(",")
        PlayerName = temp[0].strip()
        PlayerTime = temp[1].strip()
        
        if PlayerTime in d:
            d[PlayerTime].append[PlayerName]
        else:
            d[PlayerTime] = [PlayerName]
            
    for key in d.keys():
        print "%s: %s" % (key, d[key])
        
    
    
def Main():
    Rubiks = countTime("Rubiks.txt")
    
Main()
