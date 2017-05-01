import sys
sys.path.append('../Module')
import WulfModule

def NumberOfPossibilities(Weapons, Suspects):
    p = []
    for weapon in Weapons:
        for suspect in Suspects:
            p.append("%s %s" %(weapon, suspect))
    #print "There are %s possibilities." %len(p)
    return p
    
    
    
def Searching(Weapons, Suspects):
    #Possibilities = 9
    #while Possibilities != 1:
    #   NumberOfPossibilities(Weapons, Suspects)
    
    Choice = WulfModule.UserString("Is this clue about a weapon (w) or suspect (s)?")
    
    if Choice == "s":
        Suspect = WulfModule.UserString("Enter the innocent suspect (%s)" %Suspects)
        SusUpp = Suspect.upper()
        
        if SusUpp in Suspects:
            Suspects.remove(SusUpp)
            
    if Choice == "w":
        Weapon = WulfModule.UserString("Enter the weapon not used (%s)" %Weapons)
        WeapUpp = Weapon.upper()
        
        if WeapUpp in Weapons:
            Weapons.remove(WeapUpp)
        
    
    
    
def Main():
    Weapons = ['CANDLESTICK', 'ROPE', 'WRENCH']
    Suspects = ['MISS SCARLET', 'COL MUSTARD', 'MISS WHITE']
    Possibilities = NumberOfPossibilities(Weapons, Suspects)
    CluesLeft = len(Possibilities)
    while CluesLeft != 2:
        Possibilities = NumberOfPossibilities(Weapons, Suspects)
        CluesLeft = len(Possibilities)
        print "There are %s possibilities left." %CluesLeft
        Searching(Weapons, Suspects)
    if CluesLeft == 2:
        print "It was %s with %s!" %(Weapons, Suspects)
    
    
Main()