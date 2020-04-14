# LatLongDistanceCalc_Sorting
Before running, two libraries will need to be installed, Pandas & Geopy.
Installing Pandas: in the command line run the command- pip install pandas
Installing Geopy: in the command line run the command- pip install geopy
In the command line locate the InternshipScript.py file and run it using the command- python InternshipScript.py
Be sure that the locations-data.txt file is in the same folder as the InternshipScript.py file

This program reads in data from the locations-data.txt file. The program then calculates the distances from all of the locations given to the origin of the Earth, (latitude 0, longitude 0). These distances are then added to the orginial data in a new file locations-distances-data.csv where the locations are ordered from the shortest distance to the longest distance. This program implements a command line interface where the user has the choice of searching a location to get the locations distance to the origin or getting the top 5, top 10, or all locations and there distances to the origin.
