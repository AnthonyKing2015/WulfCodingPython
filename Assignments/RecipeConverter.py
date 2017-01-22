#Original Programmer: Anthony King created on January 20th, 2017
#This program will take inputted values, spit out a multiplcation of them
#and will also spit out the gram values of them as well. 

print "--Recipe Converter--"
print "Please enter the following ingredients for the original recipe"
print "Enter the amount of flour (cups):",
flour = raw_input()
print "Enter the amoutn of water (cups):",
water = raw_input()
print "Entet the amount of salt (teaspoons):",
salt = raw_input()
print "Enter the amount of yeast (teaspoons):",
yeast = raw_input()
print "Please enter the conversion factor (ex. 2.0 will double it): ",
conversion = raw_input()

print "--Converted Recipe--"
print "Flour (cups): %.2f " %(float(flour)* float(conversion))
print "Water (cups): %.2f " %(float(water)* float(conversion))
print "Salt (teaspoons): %.2f " %(float(water)* float(conversion))
print "Yeast (teaspoons): %.2F " %(float(yeast) * float(conversion))

print "--Converted Reciple in grams--"
#1 cup = 128 grams: flour
#1 cup = 240 grams: water
#1 teaspoon = 5 grams: salt
#1 teaspoon = 2.83 grams: yeast
print "Flour (grams): %.2f " %(float(flour)* float(conversion) * 128)
print "Water (grams): %.2f " %(float(water)* float(conversion) * 240)
print "Salt (grams): %.2f " %(float(water)* float(conversion) * 5)
print "Yeast (grams): %.2F " %(float(yeast) * float(conversion) * 2.83)






