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

print(address.address_lookup.get('1060 Dalton Ave S', 'N/A'))

'''if address.start_address.get('1060 Dalton Ave S') > address.start_address.get('1488 4800 S') :
    print('True')
else: print('False')'''

'''def distanceBetween(address1, address2):
    if address.address_lookup.get(address1) > address.address_lookup.get(address2) :
        print(distance_list[address.address_lookup.get(address1, 'N/A')][address.address_lookup.get(address2, 'N/A')])
    else :
        print(distance_list[address.address_lookup.get(address2, 'N/A')][address.address_lookup.get(address1, 'N/A')])'''

def distanceBetween(address1, address2):
    if address.address_lookup.get(address1) > address.address_lookup.get(address2) :
        distance_between = (distance_list[address.address_lookup.get(address1, 'N/A')][address.address_lookup.get(address2, 'N/A')])
        print(distance_between)
        return distance_between
    else :
        distance_between = (distance_list[address.address_lookup.get(address2, 'N/A')][address.address_lookup.get(address1, 'N/A')])
        print(distance_between)
        return distance_between


distanceBetween('1060 Dalton Ave S', '4001 South 700 East')
distanceBetween('195 W Oakland Ave', '2010 W 500 S')
distanceBetween('5383 S 900 East #104', '4001 South 700 East')


