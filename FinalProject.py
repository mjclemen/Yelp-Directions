"""
Created on Sat Nov 23 15:52:58 2019

@author: Mandel Clemente, mjclemen
"""

import json
import urllib.request
import re

# API key provided by Google Maps Platform
apiKey = 'AIzaSyBwbZFvTW9PXTNxDqUSr4s2Nnn0Bnx24L0'

# coordinates of CMU to use as origin: 40.4433° N, 79.9439° W
origin = '40.4433,-79.9439'

# Queens is the placeholder destination for now. Will replace with user's selected location
destination = 'Queens'

# Piece together the url using the fixed origin, the user's selected destination, and the api
# key provided by Google Maps Platform
url = 'https://maps.googleapis.com/maps/api/directions/json?origin=' + origin + '&destination='\
+ destination + '&key=' + apiKey

# Send the API Request
apiResponse = urllib.request.urlopen(url)

# Read in the JSON response from the API
jsonResponse = json.loads(apiResponse.read())

# Use the route key to receive the directions for the user
googleMapsRoutes = jsonResponse['routes']

# Go to the legs section in the routes key and begin grabbing the parts the user will want
googleMapsLegs = googleMapsRoutes[0]['legs']

# Get the time and distance that the user will travel to get to their desired location
travelTime = googleMapsLegs[0]['duration']['text']
travelDistance = googleMapsLegs[0]['distance']['text']

# The steps section of the legs contains several pieces of travel information, one being
# step-by-step instructions for the user. Directions are in default driving mode
steps = googleMapsLegs[0]['steps']

# Set up the directions variable
travelDirections = ''
for step in steps:
    # https://stackoverflow.com/questions/9662346/python-code-to-remove-html-tags-from-a-string
    # Used the link ^ to get html syntax. Will use it to remove from the driving instructions:
    htmlSyntax = re.compile('<.*?>')
    
    # Append each line of directions to be displayed to the user
    travelDirections += re.sub(htmlSyntax,'',step['html_instructions']).strip() + '\n'
    
# Print out the travel time, the distance, and the directions
print('Time: ' + travelTime)
print('Distance: ' + travelDistance)
print('Driving Directions:')
print(travelDirections)