d = {}
for line in open("Rubiks.txt"):
    temp = line.split(",")
    PlayerName = temp[0].strip()
    PlayerTime = temp[1].strip()
        
    if PlayerTime in d:
        d[PlayerTime].append[PlayerName]
    else:
        d[PlayerTime] = [PlayerName]
            
print d

print sorted(d.keys())
