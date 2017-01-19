print "How many Malcorps were there on planet Exflon?", 
exflon = raw_input()
print "How many Malcorps were there on planet Mobiles?", 
mobiles = raw_input()
print "How many Malcorps were there on planet Monsantoes?", 
monsantoes = raw_input()

totalMal = int(exflon) + int(mobiles) + int(monsantoes)
print "You found %s Malcorps" % totalMal
print "The average Malcorps is %.2f" %(totalMal/3.0)