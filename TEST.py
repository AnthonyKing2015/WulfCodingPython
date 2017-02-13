file = open('DataDuringRush.txt', 'r')
SpeedList = []
for speed in file:
    SpeedList.append(int(speed))
print SpeedList


Total = sum(SpeedList)
Length = len(SpeedList)
average = Total/Length
print average
print Length

c = 0
Fines = 0
for speed in SpeedList:
    if speed >= 69:
        c = c + 1
if fi 
    Fines = c * 150

print c
print Fines



