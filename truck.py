
import package


class Truck:
    def __init__(self):
        #self.loaded_packages = []
        self.loaded_packages = []

truck1 = Truck()
truck2 = Truck()
truck3 = Truck()

truck1.loaded_packages.append(package.package1.package_id)
truck1.loaded_packages.append(package.package13.package_id)
truck1.loaded_packages.append(package.package14.package_id)
truck1.loaded_packages.append(package.package15.package_id)
truck1.loaded_packages.append(package.package16.package_id)
truck1.loaded_packages.append(package.package19.package_id)
truck1.loaded_packages.append(package.package20.package_id)
truck1.loaded_packages.append(package.package29.package_id)
truck1.loaded_packages.append(package.package30.package_id)
truck1.loaded_packages.append(package.package31.package_id)
truck1.loaded_packages.append(package.package34.package_id)
truck1.loaded_packages.append(package.package37.package_id)
truck1.loaded_packages.append(package.package40.package_id)
print('Truck1 Packages: ', truck1.loaded_packages)

'''for pkg in truck1.loaded_packages:
    print(main.packageHash.lookup(pkg))
    #print(pkg)'''

def truckDeliverPackages(truck_number):
    import distance
    #delivered_packages = set()
    min_distance, closest_address, closest_pkg = distance.minDistanceFrom('4001 South 700 East', truck_number.loaded_packages)
    print('Closest address,', closest_address, ', is', min_distance, "miles away. Package # is:", closest_pkg)
    #print(closest_address)
    #print(closest_pkg)
    truck_number.loaded_packages.remove(closest_pkg)
    print('Package', closest_pkg, 'delivered!')
    #delivered_packages.add(closest_pkg)
    for i in range(len(truck_number.loaded_packages)):
        #if pkg not in delivered_packages:
        #print('Package not delivered yet')
        print('From:', closest_address)
        min_distance, closest_address, closest_pkg = distance.minDistanceFrom(closest_address, truck_number.loaded_packages)
        print('Closest address,', closest_address, ', is', min_distance, "miles away. Package # is:", closest_pkg)
        #print(min_distance)
        #print(closest_address)
        #print(closest_pkg)
        #delivered_packages.add(closest_pkg)
        truck_number.loaded_packages.remove(closest_pkg)
        print('Package', closest_pkg, 'delivered!')

'''for pkg in truck_number.loaded_packages:
        print(main.packageHash.lookup(pkg))'''

truckDeliverPackages(truck1)


truck2.loaded_packages.add(package.package3.package_id)
truck2.loaded_packages.add(package.package6.package_id)
truck2.loaded_packages.add(package.package18.package_id)
truck2.loaded_packages.add(package.package25.package_id)
truck2.loaded_packages.add(package.package28.package_id)
truck2.loaded_packages.add(package.package32.package_id)
truck2.loaded_packages.add(package.package36.package_id)
truck2.loaded_packages.add(package.package38.package_id)
truck2.loaded_packages.add(package.package33.package_id)
truck2.loaded_packages.add(package.package35.package_id)
truck2.loaded_packages.add(package.package39.package_id)
print('Truck2 Packages: ', truck2.loaded_packages)

truck3.loaded_packages.add(package.package2.package_id)
truck3.loaded_packages.add(package.package4.package_id)
truck3.loaded_packages.add(package.package5.package_id)
truck3.loaded_packages.add(package.package7.package_id)
truck3.loaded_packages.add(package.package8.package_id)
truck3.loaded_packages.add(package.package9.package_id)
truck3.loaded_packages.add(package.package10.package_id)
truck3.loaded_packages.add(package.package11.package_id)
truck3.loaded_packages.add(package.package12.package_id)
truck3.loaded_packages.add(package.package17.package_id)
truck3.loaded_packages.add(package.package21.package_id)
truck3.loaded_packages.add(package.package22.package_id)
truck3.loaded_packages.add(package.package23.package_id)
truck3.loaded_packages.add(package.package24.package_id)
truck3.loaded_packages.add(package.package26.package_id)
truck3.loaded_packages.add(package.package27.package_id)
print('Truck3 Packages: ', truck3.loaded_packages)



'''truck1.loaded_packages.append(package.package1.package_id)
truck1.loaded_packages.append(package.package13.package_id)
truck1.loaded_packages.append(package.package14.package_id)
truck1.loaded_packages.append(package.package15.package_id)
truck1.loaded_packages.append(package.package16.package_id)
truck1.loaded_packages.append(package.package19.package_id)
truck1.loaded_packages.append(package.package20.package_id)
truck1.loaded_packages.append(package.package29.package_id)
truck1.loaded_packages.append(package.package30.package_id)
truck1.loaded_packages.append(package.package31.package_id)
truck1.loaded_packages.append(package.package34.package_id)
truck1.loaded_packages.append(package.package37.package_id)
truck1.loaded_packages.append(package.package40.package_id)
print(truck1.loaded_packages)

truck2.loaded_packages.append(package.package3.package_id)
truck2.loaded_packages.append(package.package6.package_id)
truck2.loaded_packages.append(package.package18.package_id)
truck2.loaded_packages.append(package.package25.package_id)
truck2.loaded_packages.append(package.package28.package_id)
truck2.loaded_packages.append(package.package32.package_id)
truck2.loaded_packages.append(package.package36.package_id)
truck2.loaded_packages.append(package.package38.package_id)
print(truck2.loaded_packages)

truck3.loaded_packages.append(package.package2.package_id)
truck3.loaded_packages.append(package.package4.package_id)
truck3.loaded_packages.append(package.package5.package_id)
truck3.loaded_packages.append(package.package7.package_id)
truck3.loaded_packages.append(package.package8.package_id)
truck3.loaded_packages.append(package.package9.package_id)
truck3.loaded_packages.append(package.package10.package_id)
truck3.loaded_packages.append(package.package11.package_id)
truck3.loaded_packages.append(package.package12.package_id)
truck3.loaded_packages.append(package.package17.package_id)
truck3.loaded_packages.append(package.package21.package_id)
truck3.loaded_packages.append(package.package22.package_id)
truck3.loaded_packages.append(package.package23.package_id)
truck3.loaded_packages.append(package.package24.package_id)
truck3.loaded_packages.append(package.package26.package_id)
truck3.loaded_packages.append(package.package27.package_id)
truck3.loaded_packages.append(package.package33.package_id)
truck3.loaded_packages.append(package.package35.package_id)
truck3.loaded_packages.append(package.package39.package_id)
print(truck3.loaded_packages)'''
