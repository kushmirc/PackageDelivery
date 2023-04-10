# Kush Mirchandani, Student ID: 009926810

import package

# Defines the HashTable objects and methods.
class HashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    # space-time complexity: O(1) + O(10)
    def __init__(self, initial_capacity=10):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Inserts a new package into the hash table.
    # space-time complexity: O(2) + O(8N) + O(2)
    def insert(self, package_id, address, city, state, zip, delivery_deadline, weight, special_notes, delivery_status):  # does both insert and update
        # get the bucket list where this package will go.
        bucket = hash(package_id) % len(self.table)
        bucket_list = self.table[bucket]

        # update package if it is already in the bucket
        for pkg in bucket_list:
            # print (package)
            if pkg[0] == package_id:
                pkg[1] = address
                pkg[2] = city
                pkg[3] = state
                pkg[4] = zip
                pkg[5] = delivery_deadline
                pkg[6] = weight
                pkg[7] = special_notes
                pkg[8] = delivery_status
                return True

        # if not, insert the package to the end of the bucket list.
        package = [package_id, address, city, state, zip, delivery_deadline, weight, special_notes, delivery_status]
        bucket_list.append(package)
        return True

    # Searches for a package with matching package_id in the hash table.
    # Returns the package address if found, or None if not found.
    # space-time complexity: O(2) + O(2N)
    def lookup(self, package_id):
        # get the bucket list where this package_id would be.
        bucket = hash(package_id) % len(self.table)
        bucket_list = self.table[bucket]

        # search for the package_id in the bucket list
        for pkg in bucket_list:
            # print (key_value)
            if pkg[0] == package_id:
                return pkg[1]  # address
        return None

    # Searches for a package with matching package_id in the hash table.
    # Updates the delivery_status (including delivery time) if found, or None if not found.
    # space-time complexity: O(2) + O(3N)
    def update_delivery(self, package_id, delivery_status, time):
        # get the bucket list where this package_id would be.
        bucket = hash(package_id) % len(self.table)
        bucket_list = self.table[bucket]

        # search for the package_id in the bucket list and update the delivery_status
        for pkg in bucket_list:
            # print (key_value)
            if pkg[0] == package_id:
                pkg[8] =  delivery_status + ' ' + time
                return True

#create the hash table
# space-time complexity: O(1) + O(10)
packageHash = HashTable()

#insert all packages into the hash table
#space-time complexity: 40(O(2) + O(8N) + O(2))
packageHash.insert(package.package1.package_id, package.package1.address, package.package1.city, package.package1.state, package.package1.zip,package.package1.delivery_deadline, package.package1.weight, package.package1.special_notes, package.package1.delivery_status)
packageHash.insert(package.package2.package_id, package.package2.address, package.package2.city, package.package2.state, package.package2.zip,package.package2.delivery_deadline, package.package2.weight, package.package2.special_notes, package.package2.delivery_status)
packageHash.insert(package.package3.package_id, package.package3.address, package.package3.city, package.package3.state, package.package3.zip,package.package3.delivery_deadline, package.package3.weight, package.package3.special_notes, package.package3.delivery_status)
packageHash.insert(package.package4.package_id, package.package4.address, package.package4.city, package.package4.state, package.package4.zip,package.package4.delivery_deadline, package.package4.weight, package.package4.special_notes, package.package4.delivery_status)
packageHash.insert(package.package5.package_id, package.package5.address, package.package5.city, package.package5.state, package.package5.zip,package.package5.delivery_deadline, package.package5.weight, package.package5.special_notes, package.package5.delivery_status)
packageHash.insert(package.package6.package_id, package.package6.address, package.package6.city, package.package6.state, package.package6.zip,package.package6.delivery_deadline, package.package6.weight, package.package6.special_notes, package.package6.delivery_status)
packageHash.insert(package.package7.package_id, package.package7.address, package.package7.city, package.package7.state, package.package7.zip,package.package7.delivery_deadline, package.package7.weight, package.package7.special_notes, package.package7.delivery_status)
packageHash.insert(package.package8.package_id, package.package8.address, package.package8.city, package.package8.state, package.package8.zip,package.package8.delivery_deadline, package.package8.weight, package.package8.special_notes, package.package8.delivery_status)
packageHash.insert(package.package9.package_id, package.package9.address, package.package9.city, package.package9.state, package.package9.zip,package.package9.delivery_deadline, package.package9.weight, package.package9.special_notes, package.package9.delivery_status)
packageHash.insert(package.package10.package_id, package.package10.address, package.package10.city, package.package10.state, package.package10.zip,package.package10.delivery_deadline, package.package10.weight, package.package10.special_notes, package.package10.delivery_status)
packageHash.insert(package.package11.package_id, package.package11.address, package.package11.city, package.package11.state, package.package11.zip,package.package11.delivery_deadline, package.package11.weight, package.package11.special_notes, package.package11.delivery_status)
packageHash.insert(package.package12.package_id, package.package12.address, package.package12.city, package.package12.state, package.package12.zip,package.package12.delivery_deadline, package.package12.weight, package.package12.special_notes, package.package12.delivery_status)
packageHash.insert(package.package13.package_id, package.package13.address, package.package13.city, package.package13.state, package.package13.zip,package.package13.delivery_deadline, package.package13.weight, package.package13.special_notes, package.package13.delivery_status)
packageHash.insert(package.package14.package_id, package.package14.address, package.package14.city, package.package14.state, package.package14.zip,package.package14.delivery_deadline, package.package14.weight, package.package14.special_notes, package.package14.delivery_status)
packageHash.insert(package.package15.package_id, package.package15.address, package.package15.city, package.package15.state, package.package15.zip,package.package15.delivery_deadline, package.package15.weight, package.package15.special_notes, package.package15.delivery_status)
packageHash.insert(package.package16.package_id, package.package16.address, package.package16.city, package.package16.state, package.package16.zip,package.package16.delivery_deadline, package.package16.weight, package.package16.special_notes, package.package16.delivery_status)
packageHash.insert(package.package17.package_id, package.package17.address, package.package17.city, package.package17.state, package.package17.zip,package.package17.delivery_deadline, package.package17.weight, package.package17.special_notes, package.package17.delivery_status)
packageHash.insert(package.package18.package_id, package.package18.address, package.package18.city, package.package18.state, package.package18.zip,package.package18.delivery_deadline, package.package18.weight, package.package18.special_notes, package.package18.delivery_status)
packageHash.insert(package.package19.package_id, package.package19.address, package.package19.city, package.package19.state, package.package19.zip,package.package19.delivery_deadline, package.package19.weight, package.package19.special_notes, package.package19.delivery_status)
packageHash.insert(package.package20.package_id, package.package20.address, package.package20.city, package.package20.state, package.package20.zip,package.package20.delivery_deadline, package.package20.weight, package.package20.special_notes, package.package20.delivery_status)
packageHash.insert(package.package21.package_id, package.package21.address, package.package21.city, package.package21.state, package.package21.zip,package.package21.delivery_deadline, package.package21.weight, package.package21.special_notes, package.package21.delivery_status)
packageHash.insert(package.package22.package_id, package.package22.address, package.package22.city, package.package22.state, package.package22.zip,package.package22.delivery_deadline, package.package22.weight, package.package22.special_notes, package.package22.delivery_status)
packageHash.insert(package.package23.package_id, package.package23.address, package.package23.city, package.package23.state, package.package23.zip,package.package23.delivery_deadline, package.package23.weight, package.package23.special_notes, package.package23.delivery_status)
packageHash.insert(package.package24.package_id, package.package24.address, package.package24.city, package.package24.state, package.package24.zip,package.package24.delivery_deadline, package.package24.weight, package.package24.special_notes, package.package24.delivery_status)
packageHash.insert(package.package25.package_id, package.package25.address, package.package25.city, package.package25.state, package.package25.zip,package.package25.delivery_deadline, package.package25.weight, package.package25.special_notes, package.package25.delivery_status)
packageHash.insert(package.package26.package_id, package.package26.address, package.package26.city, package.package26.state, package.package26.zip,package.package26.delivery_deadline, package.package26.weight, package.package26.special_notes, package.package26.delivery_status)
packageHash.insert(package.package27.package_id, package.package27.address, package.package27.city, package.package27.state, package.package27.zip,package.package27.delivery_deadline, package.package27.weight, package.package27.special_notes, package.package27.delivery_status)
packageHash.insert(package.package28.package_id, package.package28.address, package.package28.city, package.package28.state, package.package28.zip,package.package28.delivery_deadline, package.package28.weight, package.package28.special_notes, package.package28.delivery_status)
packageHash.insert(package.package29.package_id, package.package29.address, package.package29.city, package.package29.state, package.package29.zip,package.package29.delivery_deadline, package.package29.weight, package.package29.special_notes, package.package29.delivery_status)
packageHash.insert(package.package30.package_id, package.package30.address, package.package30.city, package.package30.state, package.package30.zip,package.package30.delivery_deadline, package.package30.weight, package.package30.special_notes, package.package30.delivery_status)
packageHash.insert(package.package31.package_id, package.package31.address, package.package31.city, package.package31.state, package.package31.zip,package.package31.delivery_deadline, package.package31.weight, package.package31.special_notes, package.package31.delivery_status)
packageHash.insert(package.package32.package_id, package.package32.address, package.package32.city, package.package32.state, package.package32.zip,package.package32.delivery_deadline, package.package32.weight, package.package32.special_notes, package.package32.delivery_status)
packageHash.insert(package.package33.package_id, package.package33.address, package.package33.city, package.package33.state, package.package33.zip,package.package33.delivery_deadline, package.package33.weight, package.package33.special_notes, package.package33.delivery_status)
packageHash.insert(package.package34.package_id, package.package34.address, package.package34.city, package.package34.state, package.package34.zip,package.package34.delivery_deadline, package.package34.weight, package.package34.special_notes, package.package34.delivery_status)
packageHash.insert(package.package35.package_id, package.package35.address, package.package35.city, package.package35.state, package.package35.zip,package.package35.delivery_deadline, package.package35.weight, package.package35.special_notes, package.package35.delivery_status)
packageHash.insert(package.package36.package_id, package.package36.address, package.package36.city, package.package36.state, package.package36.zip,package.package36.delivery_deadline, package.package36.weight, package.package36.special_notes, package.package36.delivery_status)
packageHash.insert(package.package37.package_id, package.package37.address, package.package37.city, package.package37.state, package.package37.zip,package.package37.delivery_deadline, package.package37.weight, package.package37.special_notes, package.package37.delivery_status)
packageHash.insert(package.package38.package_id, package.package38.address, package.package38.city, package.package38.state, package.package38.zip,package.package38.delivery_deadline, package.package38.weight, package.package38.special_notes, package.package38.delivery_status)
packageHash.insert(package.package39.package_id, package.package39.address, package.package39.city, package.package39.state, package.package39.zip,package.package39.delivery_deadline, package.package39.weight, package.package39.special_notes, package.package39.delivery_status)
packageHash.insert(package.package40.package_id, package.package40.address, package.package40.city, package.package40.state, package.package40.zip,package.package40.delivery_deadline, package.package40.weight, package.package40.special_notes, package.package40.delivery_status)

#import and run the truck module
import truck