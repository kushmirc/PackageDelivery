import sys

import package
import datetime


time_obj = 0.0
time_input_hours = 24.0

'''time_input_dt = datetime.strptime(time_input, '%H:%M')
print(time_input_dt)
time_input_hours = datetime.timestamp(time_input_dt)

run_program = input('Would you like to run the package delivery program?' '\n' '  press \'y\' for yes' '\n'   '  press \'q\' for quit' '\n')
if run_program == 'q':
    sys.exit()
while run_program != 'y':
    if run_program == 'q':
        sys.exit()
    run_program = input('invalid entry, please try again' '\n')
    #continue'''

print('Please type an option number and press \'enter\' and option:')
print('-------------------------')
print('1. Print all package status and total mileage')
print('2. Get a single package status with a time')
print('3. Get all package status with a time')
print('4. Exit the program' '\n')

user_input = input()

if user_input == '2':
    package_input = int(input('Please enter a package number:' '\n'))
    while package_input < int('1') or int(package_input) > int('40'):
        package_input = int(input('Invalid package number, please try again' '\n'))
    time_input = input('Please enter a time (ex. \'10:15\')' '\n')
    time_input_split = time_input.split(":")
    time_input_hours = float(time_input_split[0]) + (float(time_input_split[1]) / 60)

if user_input == '3':
    time_input = input('Please enter a time (ex. \'10:15\')' '\n')
    time_input_split = time_input.split(":")
    time_input_hours = float(time_input_split[0]) + (float(time_input_split[1]) / 60)

if user_input == '4':
    sys.exit()
while user_input != '1' and user_input != '2' and user_input != '3':
    if user_input == '4':
        sys.exit()
    user_input = input('Invalid entry, please try again' '\n')
    #continue





class Truck:

    def __init__(self):
        #self.loaded_packages = []
        self.name = ''
        self.loaded_packages = []
        self.time = 0.0
        self.miles = 0.0

def  timeToDeliver(distance):  #time measured in hours
    time_to_deliver = distance / 18
    #print(time_to_deliver)
    return time_to_deliver


#timeToDeliver(9)

truck1 = Truck()
truck1.name = 'Truck 1'
truck1.time = 8.0
#print (str(datetime.timedelta(hours= truck1.time))) # [:-3])
truck2 = Truck()
truck2.name = 'Truck 2'
truck2.time = 9.0833333333334
truck3 = Truck()
truck3.name = 'Truck 3'
truck3.time = 10.33333333334

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
#print('Truck1 Packages: ', truck1.loaded_packages)

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
#print('Truck2 Packages: ', truck2.loaded_packages)

def loadTruck3():
    import main
    if time_input_hours == 24.0:
        print('We were informed at 10:20am that the address originally provided for package number 9 is incorrect.  The correct address is 410 S State St., Salt Lake City, UT 84111. The address is being corrected now.')
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
#print('Truck3 Packages: ', truck3.loaded_packages)

def truckDeliverPackages(truck_number):
    import distance
    import main
    global time_obj
    #delivered_packages = set()
    min_distance, closest_address, closest_pkg = distance.minDistanceFrom('4001 South 700 East', truck_number.loaded_packages)
    truck_number.miles = truck_number.miles + min_distance
    truck_number.time = truck_number.time + timeToDeliver(min_distance)
    time_obj = truck_number.time
    if time_obj > time_input_hours:
            return
    #truck_number.miles = float(decimal.Decimal(truck_number.miles)) + float(decimal.Decimal.min_distance)
    '''print('Closest address,', closest_address, ', is', min_distance, "miles away. Package # is:", closest_pkg, '. Truck miles is:', truck_number.miles, ". Truck time is:", truck_number.time, '.', 'time_obj is:', time_obj)'''
    if time_input_hours == 24.0:
        print(truck_number.name, 'has delivered package #', closest_pkg, 'to', closest_address, 'at', str(datetime.timedelta(hours=truck_number.time)))
    #print(closest_address)
    #print(closest_pkg)
    truck_number.loaded_packages.remove(closest_pkg)
    main.packageHash.update_delivery(closest_pkg, 'delivered', str(datetime.timedelta(hours= truck_number.time)))
    #print('Package', closest_pkg, 'delivered!')
    #delivered_packages.add(closest_pkg)
    for i in range(len(truck_number.loaded_packages)):
        #if pkg not in delivered_packages:
        #print('Package not delivered yet')
        min_distance, closest_address, closest_pkg = distance.minDistanceFrom(closest_address, truck_number.loaded_packages)
        truck_number.miles = truck_number.miles + min_distance
        truck_number.time = truck_number.time + timeToDeliver(min_distance)
        time_obj = truck_number.time
        if time_obj > time_input_hours:
            return
        '''print('Closest address,', closest_address, ', is', min_distance, "miles away. Package # is:", closest_pkg, '. Truck miles is:', truck_number.miles, ". Truck time is:", truck_number.time, '.', 'time_obj is:', time_obj)'''
        if time_input_hours == 24.0:
            print(truck_number.name, 'has delivered package #', closest_pkg, 'to', closest_address, 'at', str(datetime.timedelta(hours=truck_number.time)))
        #print(min_distance)
        #print(closest_address)
        #print(closest_pkg)
        #delivered_packages.add(closest_pkg)
        truck_number.loaded_packages.remove(closest_pkg)
        main.packageHash.update_delivery(closest_pkg, 'delivered', str(datetime.timedelta(hours=truck_number.time)))
        #print('Package', closest_pkg, 'delivered!')
    truck_number.miles = truck_number.miles + distance.distanceBetween(closest_address, '4001 South 700 East')
    truck_number.time = truck_number.time + timeToDeliver(min_distance)
    time_obj = truck_number.time

if time_input_hours > truck1.time:
    loadTruck1()
    truckDeliverPackages(truck1)
#print(str(datetime.timedelta(hours=time_obj)))
#print()
if time_input_hours > truck2.time:
    loadTruck2()
    truckDeliverPackages(truck2)
#print(str(datetime.timedelta(hours=time_obj)))
#print()

if time_input_hours > truck3.time:
    loadTruck3()
    truckDeliverPackages(truck3)
print()

if time_input_hours != 24.0:
    import main
    if user_input == '3':
        for bucket in main.packageHash.table:
            for pkg in bucket:
                print(pkg)
    elif user_input == '2':
        for bucket in main.packageHash.table:
            for pkg in bucket:
                if pkg[0] == package_input:
                    print(pkg)

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
    #print('Total drive time to deliver all packages: ')