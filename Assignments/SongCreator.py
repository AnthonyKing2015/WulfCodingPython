#SongCreator Program
#Programmed by Anthony King on 1/28/2017
#This program will take inputted values, display them via a list then in "song format"

import sys
sys.path.append('../Module')
import WulfModule

SongLyrics = []
Verse1 = WulfModule.UserString("Please enter the first verse: ")
Verse2 = WulfModule.UserString("Please enter the second verse:  ")
Verse3 = WulfModule.UserString("Please enter the third verse:  ")
Verse4 = WulfModule.UserString("Please enter the fourth verse:  ")
Chorus = WulfModule.UserString("Please enter the chorus: " + " ")
ChorusRepeat = WulfModule.UserInt("Please enter the chorus repeat (ex. 2 will make the chorus repeat twice): ")

SongLyrics.append(Verse1)
SongLyrics.append(Chorus*ChorusRepeat)
SongLyrics.append(Verse2)
SongLyrics.append(Chorus*ChorusRepeat)
SongLyrics.append(Verse3)
SongLyrics.append(Chorus*ChorusRepeat)
SongLyrics.append(Verse4)
SongLyrics.append(Chorus*ChorusRepeat)
print SongLyrics

print Verse1
print Chorus * ChorusRepeat
print Verse2
print Chorus * ChorusRepeat
print Verse3
print Chorus * ChorusRepeat
print Verse4
print Chorus * ChorusRepeat
print "--One more time!--"
print Verse1
print Chorus * ChorusRepeat
print Verse2
print Chorus * ChorusRepeat
print Verse3
print Chorus * ChorusRepeat
print Verse4
print Chorus * ChorusRepeat
