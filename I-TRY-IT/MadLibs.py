import sys
sys.path.append('../Module')
import WulfModule

sentence = ("Let's build a snowman! First we need to have a really ADJ1 snowstorm, of course"
            " on an ADJ2 day. Watching all that CLR1 snow fall makes me VRB1 for a bowl of ADJ3"
            " VGT1! EXCL1 it's still VRB2 and there's a lot of it. Let's go! Next is VRB3 to go "
            " out in the cold. Once that is done, we need to get busy. We make a NOUN1 and VRB4"
            " PLC1. It gets so ADJ4 we can't roll in it anymore!")
            
ADJ1 = WulfModule.UserString("Enter an adjective:")
ADJ2 = WulfModule.UserString("Enter an adjective:")
CLR1 = WulfModule.UserString("Enter a color:")
VRB1 = WulfModule.UserString("Enter a verb:")
ADJ3 = WulfModule.UserString("Enter an adjective:")
VGT1 = WulfModule.UserString("Enter a vegetable:")
EXCL1 = WulfModule.UserString("Enter an exclamation:")
VRB2 = WulfModule.UserString("Enter a verb ending in -ing:")
VRB3 = WulfModule.UserString("Enter a verb ending in -ing:")
NOUN1 = WulfModule.UserString("Enter a noun:")
VRB4 = WulfModule.UserString("Enter a verb:")
PLC1 = WulfModule.UserString("Enter a place:")
ADJ4 = WulfModule.UserString("Enter an adjective:")

print

sentence = sentence.replace("ADJ1", ADJ1)
sentence = sentence.replace("ADJ2", ADJ2)
sentence = sentence.replace("CLR1", CLR1)
sentence = sentence.replace("VRB1", VRB1)
sentence = sentence.replace("ADJ3", ADJ3)
sentence = sentence.replace("VGT1", VGT1)
sentence = sentence.replace("EXCL1", EXCL1)
sentence = sentence.replace("VRB2", VRB2)
sentence = sentence.replace("VRB3", VRB3)
sentence = sentence.replace("NOUN1", NOUN1)
sentence = sentence.replace("VRB4", VRB4)
sentence = sentence.replace("PLC1", PLC1)
sentence = sentence.replace("ADJ4", ADJ4)

print sentence
