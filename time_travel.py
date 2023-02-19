import json #collection and formatting of data
import urllib.request #need to open URL's
from urllib.request import urlopen
import math

#there should be no spaces in the address. They should be replaced with + characters
origin = "502+East+Kingsley+Street,+Ann+Arbor,+MI"
destination = "29201+Telegraph+Rd,+Southfield,+MI+48034"

#An API key is necessary to allow access
API_KEY = "AIzaSyATjsY5asJnxbhpQwXM8bWIJV9Mhkng09c" #this is my personal key that I created

#returns distance and travelling time in minutes
#there should be no spaces in the address. They should be replaced with + characters
def getResponseFromGoogleAndLogResult1(origin, destination):
    # Create a URL to use google API url 
    url1 = "https://maps.googleapis.com/maps/api/distancematrix/json?origins="+origin+"&destinations="+destination+"&key=" + API_KEY
    with urllib.request.urlopen(url1) as url:
        data = json.load(url)

    drive_time = round(data['rows'][0]['elements'][0]['duration']['value']/60, 1) #convert seconds to minutes and round to 1 decimals
    dist = round(data['rows'][0]['elements'][0]['distance']['value']/1609, 1) #convert meters to miles and round to 1 decimals
    info = [drive_time, dist]
    return info


travelling_info = getResponseFromGoogleAndLogResult1(origin, destination)
print(travelling_info)



#--------------------------------------------------------------------------
#an alternative version using directions instead of distance matrix
def getResponseFromGoogleAndLogResult2(origin, destination):
    # Create a URL to use google API url 
    url2 = "https://maps.googleapis.com/maps/api/directions/json?origin="+ origin +"&destination="+destination+"&key=" + API_KEY
    with urllib.request.urlopen(url2) as url:
        data = json.load(url)

    #get the driving time in seconds
    drive_time = math.ceil(data['routes'][0]['legs'][0]['duration']['value']/60)
    #get distance information
    dist = data['routes'][0]['legs'][0]['distance']['text']
    info = [drive_time, dist]
    return info
