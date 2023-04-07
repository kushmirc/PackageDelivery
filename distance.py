# Read distanceCSV file
import csv
import address



with open("distanceCSV.csv", encoding='utf-8-sig') as fp:
    reader = csv.reader(fp, delimiter=",", quotechar='"' )
    # next(reader, None)  # skip the headers
    distance_list = [row for row in reader]
    #for row in reader:
        #print(row)

#print(distance_list)
#print(distance_list[1][0])



'''def distanceBetween(address1, address2):
    print(distance_list[address.start_address.get(address1, 'N/A')][address.end_address[address1].get(address2, 'N/A')])'''

#print(address.address_lookup.get('1060 Dalton Ave S', 'N/A'))

'''if address.start_address.get('1060 Dalton Ave S') > address.start_address.get('1488 4800 S') :
    print('True')
else: print('False')'''

'''def distanceBetween(address1, address2):
    if address.address_lookup.get(address1) > address.address_lookup.get(address2) :
        print(distance_list[address.address_lookup.get(address1, 'N/A')][address.address_lookup.get(address2, 'N/A')])
    else :
        print(distance_list[address.address_lookup.get(address2, 'N/A')][address.address_lookup.get(address1, 'N/A')])'''

def distanceBetween(address1, address2):
    if address.address_lookup.get(address1) > address.address_lookup.get(address2):
        distance_between = float((distance_list[address.address_lookup.get(address1, 'N/A')][address.address_lookup.get(address2, 'N/A')]))
        #print(distance_between)
        return distance_between
    else:
        distance_between = float((distance_list[address.address_lookup.get(address2, 'N/A')][address.address_lookup.get(address1, 'N/A')]))
        #print(distance_between)
        return distance_between


#distanceBetween('1060 Dalton Ave S', '4001 South 700 East')
#distanceBetween('195 W Oakland Ave', '2010 W 500 S')


def minDistanceFrom(fromAddress, truckPackages):
    import main
    min_distance = 100.0
    closest_address = ''
    closest_pkg = 0
    for pkg in truckPackages:
        if distanceBetween(fromAddress, main.packageHash.lookup(pkg)) < min_distance:
            min_distance = distanceBetween(fromAddress, main.packageHash.lookup(pkg))
            closest_address = main.packageHash.lookup(pkg)
            closest_pkg = pkg
    #print('Closest Address is:', closest_address)
    #print('Min Distance is:', min_distance)
    return min_distance, closest_address, closest_pkg

'''import truck
min_distance, closest_address = minDistanceFrom('4001 South 700 East', truck.truck1.loaded_packages)
print(min_distance)'''

#import truck
#minDistanceFrom('4001 South 700 East', truck.truck1.loaded_packages)


