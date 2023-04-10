# Read distanceCSV file and create a 2d list of distances.
#space-time complexity: O(N^2)

import csv
import address

with open("distanceCSV.csv", encoding='utf-8-sig') as fp:
    reader = csv.reader(fp, delimiter=",", quotechar='"' )
    # next(reader, None)  # skip the headers
    distance_list = [row for row in reader]
    #for row in reader:
        #print(row)

#Define a method to find the distance between two addresses passed in.
#space-time complexity: O(3)
def distanceBetween(address1, address2):
    #Distances are given in only one direction on the distanceCSV.
    #This checks if the addresses are going in the right direction, and returns the corresponding distance.
    if address.address_lookup.get(address1) > address.address_lookup.get(address2):
        distance_between = float((distance_list[address.address_lookup.get(address1, 'N/A')][address.address_lookup.get(address2, 'N/A')]))
        return distance_between
    #if the addresses are going in the wrong direction this flips the addresses around to find the distance.
    else:
        distance_between = float((distance_list[address.address_lookup.get(address2, 'N/A')][address.address_lookup.get(address1, 'N/A')]))
        return distance_between

#Define a method to find the nearest package delivery address from among all of those remaining in the truck.
#This is the heart of the core algorithm using a "nearest neighbor" approach.
#space-time complexity: (O(3)) + (O(3(N + 2)))
def minDistanceFrom(fromAddress, truckPackages):
    import main
    #set the min_distance to a number higher than any distance found in the distanceCSV.
    min_distance = 100.0
    closest_address = ''
    closest_pkg = 0
    for pkg in truckPackages:
        #loop through all of the packages in the truck using the distanceBetween method from above,
        #look for the smaller distance at each iteration and set that distance as the min_distance value.
        if distanceBetween(fromAddress, main.packageHash.lookup(pkg)) < min_distance:
            min_distance = distanceBetween(fromAddress, main.packageHash.lookup(pkg))
            closest_address = main.packageHash.lookup(pkg)
            closest_pkg = pkg
    #return a multiple-value tuple providing access to each variable set by the loop.
    return min_distance, closest_address, closest_pkg
