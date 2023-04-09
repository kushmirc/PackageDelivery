#A module to create and load trucks, and run the core of the program.
import sys
import package
import datetime

#Define time object and initialize it to a zero value.
time_obj = 0.0
#Define a varible to hold the time value input by the user and initialize it to a value always greater than the time_obj.
time_input_hours = 24.0

#Display a starting menu in the command prompt
print('Please type an option number and press \'enter\' and option:')
print('-------------------------')
print('1. Print all package status and total mileage')
print('2. Get a single package status with a time')
print('3. Get all package status with a time')
print('4. Exit the program' '\n')

#capture the selection made by the user.
user_input = input()

#if the user enters an invalid option, display an error message and wait for another input.
#if the user quits by entering 4 at any point, quit the program.
#if the user enters 1, run the program.
while user_input != '1' and user_input != '2' and user_input != '3':
    if user_input == '4':
        sys.exit()
    user_input = input('Invalid entry, please try again' '\n')

#if the user enters 2, capture a package number and time value to look up.
if user_input == '2':
    package_input = int(input('Please enter a package number:' '\n'))
    while package_input < int('1') or int(package_input) > int('40'):
        package_input = int(input('Invalid package number, please try again' '\n'))
    time_input = input('Please enter a time (ex. \'10:15\')' '\n')
    #convert the time string from the user to a float value for hours by first splitting at the semicolon.
    #then convert each split portion to a float, divide the minutes by 60, and add them together.
    time_input_split = time_input.split(":")
    time_input_hours = float(time_input_split[0]) + (float(time_input_split[1]) / 60)

#if the user enters 3, capture a time value to look up.
if user_input == '3':
    time_input = input('Please enter a time (ex. \'10:15\')' '\n')
    #this is the same string-to-float time conversion described above.
    time_input_split = time_input.split(":")
    time_input_hours = float(time_input_split[0]) + (float(time_input_split[1]) / 60)

#Define the Truck class with a constructor to instantiate Truck objects.
class Truck:
    def __init__(self):
        self.name = ''
        self.loaded_packages = []
        self.time = 0.0
        self.miles = 0.0

#Calculate the time taken to deliver a package (as a float in hours) with a given distance assuming trucks always drive at 18mph.
def  timeToDeliver(distance):
    time_to_deliver = distance / 18  #time measured in hours
    return time_to_deliver


#Instantiate Truck1, set its name, and set its departure time from the hub.
truck1 = Truck()
truck1.name = 'Truck 1'
truck1.time = 8.0

#Instantiate Truck2, set its name, and set its departure time from the hub.
truck2 = Truck()
truck2.name = 'Truck 2'
truck2.time = 9.0833333333334

#Instantiate Truck3, set its name, and set its departure time from the hub.
truck3 = Truck()
truck3.name = 'Truck 3'
truck3.time = 10.33333333334

#define a method to load the packages that will go on Truck 1.
def loadTruck1():
    import main
    truck1.loaded_packages.append(package.package1.package_id)
    main.packageHash.update_delivery(1, 'en route', '')
    truck1.loaded_packages.append(package.package13.package_id)
    main.packageHash.update_delivery(13, 'en route', '')
    truck1.loaded_packages.append(package.package14.package_id)
    main.packageHash.update_delivery(14, 'en route', '')
    truck1.loaded_packages.append(package.package15.package_id)
    main.packageHash.update_delivery(15, 'en route', '')
    truck1.loaded_packages.append(package.package16.package_id)
    main.packageHash.update_delivery(16, 'en route', '')
    truck1.loaded_packages.append(package.package19.package_id)
    main.packageHash.update_delivery(17, 'en route', '')
    truck1.loaded_packages.append(package.package20.package_id)
    main.packageHash.update_delivery(20, 'en route', '')
    truck1.loaded_packages.append(package.package29.package_id)
    main.packageHash.update_delivery(29, 'en route', '')
    truck1.loaded_packages.append(package.package30.package_id)
    main.packageHash.update_delivery(30, 'en route', '')
    truck1.loaded_packages.append(package.package31.package_id)
    main.packageHash.update_delivery(31, 'en route', '')
    truck1.loaded_packages.append(package.package34.package_id)
    main.packageHash.update_delivery(34, 'en route', '')
    truck1.loaded_packages.append(package.package37.package_id)
    main.packageHash.update_delivery(37, 'en route', '')
    truck1.loaded_packages.append(package.package40.package_id)
    main.packageHash.update_delivery(40, 'en route', '')

#define a method to load the packages that will go on Truck 2.
def loadTruck2():
    import main
    truck2.loaded_packages.append(package.package3.package_id)
    main.packageHash.update_delivery(3, 'en route', '')
    truck2.loaded_packages.append(package.package6.package_id)
    main.packageHash.update_delivery(6, 'en route', '')
    truck2.loaded_packages.append(package.package18.package_id)
    main.packageHash.update_delivery(18, 'en route', '')
    truck2.loaded_packages.append(package.package25.package_id)
    main.packageHash.update_delivery(25, 'en route', '')
    truck2.loaded_packages.append(package.package28.package_id)
    main.packageHash.update_delivery(28, 'en route', '')
    truck2.loaded_packages.append(package.package32.package_id)
    main.packageHash.update_delivery(32, 'en route', '')
    truck2.loaded_packages.append(package.package33.package_id)
    main.packageHash.update_delivery(33, 'en route', '')
    truck2.loaded_packages.append(package.package35.package_id)
    main.packageHash.update_delivery(35, 'en route', '')
    truck2.loaded_packages.append(package.package36.package_id)
    main.packageHash.update_delivery(36, 'en route', '')
    truck2.loaded_packages.append(package.package38.package_id)
    main.packageHash.update_delivery(38, 'en route', '')
    truck2.loaded_packages.append(package.package39.package_id)
    main.packageHash.update_delivery(39, 'en route', '')

#define a method to load the packages that will go on Truck 3.
#since a package from Truck 3 will have a special message, display the message when the full program is run
#(the full program runs when there is no time input by the user, a.k.a., option 1).
def loadTruck3():
    import main
    if time_input_hours == 24.0:
        print('We were informed at 10:20am that the address originally provided for package number 9 is incorrect.  The correct address is 410 S State St., Salt Lake City, UT 84111. The address is being corrected now.')
    #update package 9 per the special instructions.
    main.packageHash.insert(package.package9.package_id, '410 S State St', package.package9.city, package.package9.state, '84111', package.package9.delivery_deadline, package.package9.weight, package.package9.special_notes, package.package9.delivery_status)
    truck3.loaded_packages.append(package.package2.package_id)
    main.packageHash.update_delivery(2, 'en route', '')
    truck3.loaded_packages.append(package.package4.package_id)
    main.packageHash.update_delivery(4, 'en route', '')
    truck3.loaded_packages.append(package.package5.package_id)
    main.packageHash.update_delivery(5, 'en route', '')
    truck3.loaded_packages.append(package.package7.package_id)
    main.packageHash.update_delivery(7, 'en route', '')
    truck3.loaded_packages.append(package.package8.package_id)
    main.packageHash.update_delivery(8, 'en route', '')
    truck3.loaded_packages.append(package.package9.package_id)
    main.packageHash.update_delivery(9, 'en route', '')
    truck3.loaded_packages.append(package.package10.package_id)
    main.packageHash.update_delivery(10, 'en route', '')
    truck3.loaded_packages.append(package.package11.package_id)
    main.packageHash.update_delivery(11, 'en route', '')
    truck3.loaded_packages.append(package.package12.package_id)
    main.packageHash.update_delivery(12, 'en route', '')
    truck3.loaded_packages.append(package.package17.package_id)
    main.packageHash.update_delivery(17, 'en route', '')
    truck3.loaded_packages.append(package.package21.package_id)
    main.packageHash.update_delivery(21, 'en route', '')
    truck3.loaded_packages.append(package.package22.package_id)
    main.packageHash.update_delivery(22, 'en route', '')
    truck3.loaded_packages.append(package.package23.package_id)
    main.packageHash.update_delivery(23, 'en route', '')
    truck3.loaded_packages.append(package.package24.package_id)
    main.packageHash.update_delivery(24, 'en route', '')
    truck3.loaded_packages.append(package.package26.package_id)
    main.packageHash.update_delivery(26, 'en route', '')
    truck3.loaded_packages.append(package.package27.package_id)
    main.packageHash.update_delivery(27, 'en route', '')

#This is the core algorithm which implements the "nearest neighbor" algorithm accomplished by looping the minDistanceFrom function.
def truckDeliverPackages(truck_number):
    import distance
    import main
    global time_obj
    #The first address is always the hub, so the minDistanceFrom is run once at the beginning from the hub.
    min_distance, closest_address, closest_pkg = distance.minDistanceFrom('4001 South 700 East', truck_number.loaded_packages)
    #add the miles to the first nearest address to the miles traveled by the truck.
    truck_number.miles = truck_number.miles + min_distance
    #add the time to the first nearest address to the time traveled by the truck.
    truck_number.time = truck_number.time + timeToDeliver(min_distance)
    #update the global time object to reflect the latest time for the truck.
    time_obj = truck_number.time
    #check to see if the time input by the user is prior to the truck's time after delivering the package.
    #if so, exit the function because no more deliveries should be made at this point.
    if time_obj > time_input_hours:
            return
    #if the user hasn't entered a time (they chose option 1), then log the delivery for the full report.
    if time_input_hours == 24.0:
        print(truck_number.name, 'has delivered package #', closest_pkg, 'to', closest_address, 'at', str(datetime.timedelta(hours=truck_number.time)))
    #now that the package has been delivered, remove it from the truck.
    truck_number.loaded_packages.remove(closest_pkg)
    #update the delivery status of the delivered package in the hash table.
    main.packageHash.update_delivery(closest_pkg, 'delivered', str(datetime.timedelta(hours= truck_number.time)))
    #for the remainder of the packages in the truck, look through the minDistanceFrom function (nearest neighbor)
    #to deliver to the next nearest package address at each iteration, using the previous address as the From Address.
    #the rest of the loop works the same as the steps above.
    for i in range(len(truck_number.loaded_packages)):
        min_distance, closest_address, closest_pkg = distance.minDistanceFrom(closest_address, truck_number.loaded_packages)
        truck_number.miles = truck_number.miles + min_distance
        truck_number.time = truck_number.time + timeToDeliver(min_distance)
        time_obj = truck_number.time
        if time_obj > time_input_hours:
            return
        if time_input_hours == 24.0:
            print(truck_number.name, 'has delivered package #', closest_pkg, 'to', closest_address, 'at', str(datetime.timedelta(hours=truck_number.time)))
        truck_number.loaded_packages.remove(closest_pkg)
        main.packageHash.update_delivery(closest_pkg, 'delivered', str(datetime.timedelta(hours=truck_number.time)))
    #once loaded_packages list is empty (all packages delivered) the look will end, and the truck will travel back to the hub.
    #add the miles and the time for the trip back to the hub, and update the global time object.
    truck_number.miles = truck_number.miles + distance.distanceBetween(closest_address, '4001 South 700 East')
    truck_number.time = truck_number.time + timeToDeliver(distance.distanceBetween(closest_address, '4001 South 700 East'))
    time_obj = truck_number.time

#load truck 1 and deliver its packages if the time input is either the default value, or if it's after the departure time of the truck.
if time_input_hours > truck1.time:
    loadTruck1()
    truckDeliverPackages(truck1)

#load truck 2 and deliver its packages if the time input is either the default value, or if it's after the departure time of the truck.
if time_input_hours > truck2.time:
    loadTruck2()
    truckDeliverPackages(truck2)

#load truck 3 and deliver its packages if the time input is either the default value, or if it's after the departure time of the truck.
if time_input_hours > truck3.time:
    loadTruck3()
    truckDeliverPackages(truck3)
print()

#run these statements if the user chose option 2 or 3 (time_input_hours is not the default value):
if time_input_hours != 24.0:
    import main
    #for option 3, print the information for all of the packages in the hash table.
    if user_input == '3':
        for bucket in main.packageHash.table:
            for pkg in bucket:
                print(pkg)
    #for option 2, print the information for just the package number input by the user.
    elif user_input == '2':
        for bucket in main.packageHash.table:
            for pkg in bucket:
                if pkg[0] == package_input:
                    print(pkg)

#print truck reports and total mileage if the user chose option 1 (time_input_hours remains as the default value):
if time_input_hours == 24.0:
    print('Truck 1 Report:')
    print('------------------------')
    print('Departure Time:  8:00:00')
    print('Return Time:    %s' % str(datetime.timedelta(hours= truck1.time)))
    print('Drive Time:      %s' % str(datetime.timedelta(hours= (truck1.time - 8.0))))
    print('Miles Driven:       %s' % truck1.miles)
    print()

    print('Truck 2 Report:')
    print('------------------------')
    print('Departure Time:  9:05:00')
    print('Return Time:    %s' % str(datetime.timedelta(hours= truck2.time)))
    print('Drive Time:      %s' % str(datetime.timedelta(hours= (truck2.time - 9.0833333333334))))
    print('Miles Driven:       %s' % truck2.miles)
    print()

    print('Truck 3 Report:')
    print('------------------------')
    print('Departure Time: 10:20:00')
    print('Return Time:    %s' % str(datetime.timedelta(hours= truck3.time)))
    print('Drive Time:      %s' % str(datetime.timedelta(hours= (truck3.time - 10.33333333334))))
    print('Miles Driven:       %s' % truck3.miles)
    print()

    print('Total miles driven by all trucks: %s' % (truck1.miles + truck2.miles + truck3.miles))
