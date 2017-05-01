Weapons = ['CANDLESTICK', 'ROPE', 'WRENCH']
Suspects = ['MISS SCARLET', 'COL MUSTARD', 'MISS WHITE']
p = []
for weapon in Weapons:
    for suspect in Suspects:
        p.append("%s %s" %(weapon, suspect))
print len(p)