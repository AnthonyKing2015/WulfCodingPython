import sys
sys.path.append('../Module')
import WulfModule

# ------------------------------------------------------------
# Reads the specified file (filename) and returns a dictionary 
# whose keys are bird names and whose values are the number of 
# times the bird has been seen.
# ------------------------------------------------------------
def countBirds(filename):
    d = {}
    for line in open(filename):
        temp = line.split(",")
        birdsName = temp[0].strip()
        birdCount = int(temp[1].strip())
        if birdsName in d:
            d[birdsName] += birdCount
        else: 
            d[birdsName] = birdCount
    return d
# ------------------------------------------------------------
# Asks the user to enter a bird name and then looks up 
# the sighting count for that bird in the specified 
# dictionary (d).
# ------------------------------------------------------------
def askUser(d):
    n = WulfModule.UserString("Enter the bird's name:")
    if n in d:
        print "%s has been seen %s time(s)" %(n, d[n])
    else: 
        print "%s has been seen 0 time(s)" %n
    

def main():
    birds = countBirds("Birds.txt")
    askUser(birds)
    
main()  