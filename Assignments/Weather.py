import urllib2
import json
import sys
sys.path.append('../Module')
import WulfModule

def URLMaker():
    End = WulfModule.UserString("Enter a zipcode or city name:")
    url = 'https://api.apixu.com/v1/current.json?key=08f80aa5d6e640e894e220732172404&q=' + End
    jsonTxt = urllib2.urlopen(url).read()
    Weather = json.loads(jsonTxt)
    return Weather
    
    
def PrintInfo(Weather):
    print "Displaying the weather for %s" %Weather['location']['name']
    print "Temperature: %s" %Weather['current']['temp_f']
    print "Real Fee: %s" %Weather['current']['feelslike_f']
    

def main():
    Answer = False
    while Answer == False:
        FindWeather = URLMaker()
        PrintInfo(FindWeather)
        Again = WulfModule.UserString("Do you want to search another location?")
        if Again == 'n':
            Answer = True
        
    
    
    
main()

