# ------------------------------------------------------
# reads the speeds in the specified file (filename)
# and returns them as a list of integers
# ------------------------------------------------------
def readData(filename):
    SpeedList = []
    file = open(filename)
    for speed in file: 
        SpeedList.append(int(speed))
    return SpeedList
    
# ------------------------------------------------------    
# calculates and returns the average of the numbers
# in the the specified list (l)
# ------------------------------------------------------
def getAverage(SpeedList):
    total = sum(SpeedList)
    length = len(SpeedList)
    averageoflist = (float(total) / length)
    return averageoflist
    
    
# ------------------------------------------------------
# counts and returns the number of values in the 
# specified list (l) that are greater than or 
# equal to maxSpeed
# ------------------------------------------------------
def countSpeeders(SpeedList, maxSpeed):
    count = 0
    for speed in SpeedList:
        if speed >= maxSpeed:
            count = count + 1
    return count
    
    
# ------------------------------------------------------
# Determines the number of people speeding during 
# rush hour and not during rush hour.  Also determines
# the total fines during rush hour and not during 
# rush hour.  A person is considered speeding if they
# are traveling faster than 69 MPH.  The fine for 
# speeding during rush hour is $150.  The fine for 
# speeding not during rush hour is $100.
#
# THE CORRECT OUTPUT IS:
#
# The average speed during rush hour was 63.47.
# The average speed not during rush hour was 64.07.
# There were 4 speeders during rush hour.  Total fine = $600
# There were 6 speeders not during rush hour.  Total fine = $600
# ------------------------------------------------------
def main():
    SpeedList = readData("DataDuringRush.txt")
    averageoflist = getAverage(SpeedList)
    count = countSpeeders(SpeedList, 70)
    print "The average speed during rush hour was %.2f" %averageoflist
    print "There was a total of %s speeders during rush hour." %count
    print "Total fine = $600"
    
    SpeedList = readData("DataNotDuringRush.txt")
    averageoflist = getAverage(SpeedList)
    count = countSpeeders(SpeedList, 70)
    print "The average speed not during rush hour was %.2f" %averageoflist
    print "There was a total of %s speeders during rush hour." %count
    print "Total fine = $600"
    
    

# ------------------------------------------------------
# kick off the program by calling main
# ------------------------------------------------------
main()