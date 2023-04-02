import package



class HashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=10):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Inserts a new package into the hash table.
    def insert(self, package_id, address):  # does both insert and update
        # get the bucket list where this package will go.
        bucket = hash(package_id) % len(self.table)
        bucket_list = self.table[bucket]

        # update package if it is already in the bucket
        for pkg in bucket_list:
            # print (package)
            if pkg[0] == package_id:
                pkg[1] = address
                return True

        # if not, insert the package to the end of the bucket list.
        package = [package_id, address]
        bucket_list.append(package)
        return True

    # Searches for a package with matching package_id in the hash table.
    # Returns the package if found, or None if not found.

    def lookup(self, package_id):
        # get the bucket list where this package_id would be.
        bucket = hash(package_id) % len(self.table)
        bucket_list = self.table[bucket]
        # print(bucket_list)

        # search for the package_id in the bucket list
        for pkg in bucket_list:
            # print (key_value)
            if pkg[0] == package_id:
                return pkg[1]  # value
        return None

packageHash = HashTable()

print("\nInsert Packages to Hash Table:")
packageHash.insert(package.package1.package_id, package.package1.address)
packageHash.insert(package.package2.package_id, package.package2.address)
packageHash.insert(package.package3.package_id, package.package3.address)
packageHash.insert(package.package4.package_id, package.package4.address)
packageHash.insert(package.package5.package_id, package.package5.address)
packageHash.insert(package.package6.package_id, package.package6.address)
packageHash.insert(package.package7.package_id, package.package7.address)
packageHash.insert(package.package8.package_id, package.package8.address)
packageHash.insert(package.package9.package_id, package.package9.address)
packageHash.insert(package.package10.package_id, package.package10.address)
packageHash.insert(package.package11.package_id, package.package11.address)
packageHash.insert(package.package12.package_id, package.package12.address)
packageHash.insert(package.package13.package_id, package.package13.address)
packageHash.insert(package.package14.package_id, package.package14.address)
packageHash.insert(package.package15.package_id, package.package15.address)
packageHash.insert(package.package16.package_id, package.package16.address)
packageHash.insert(package.package17.package_id, package.package17.address)
packageHash.insert(package.package18.package_id, package.package18.address)
packageHash.insert(package.package19.package_id, package.package19.address)
packageHash.insert(package.package20.package_id, package.package20.address)
packageHash.insert(package.package21.package_id, package.package21.address)
packageHash.insert(package.package22.package_id, package.package22.address)
packageHash.insert(package.package23.package_id, package.package23.address)
packageHash.insert(package.package24.package_id, package.package24.address)
packageHash.insert(package.package25.package_id, package.package25.address)
packageHash.insert(package.package26.package_id, package.package26.address)
packageHash.insert(package.package27.package_id, package.package27.address)
packageHash.insert(package.package28.package_id, package.package28.address)
packageHash.insert(package.package29.package_id, package.package29.address)
packageHash.insert(package.package30.package_id, package.package30.address)
packageHash.insert(package.package31.package_id, package.package31.address)
packageHash.insert(package.package32.package_id, package.package32.address)
packageHash.insert(package.package33.package_id, package.package33.address)
packageHash.insert(package.package34.package_id, package.package34.address)
packageHash.insert(package.package35.package_id, package.package35.address)
packageHash.insert(package.package36.package_id, package.package36.address)
packageHash.insert(package.package37.package_id, package.package37.address)
packageHash.insert(package.package38.package_id, package.package38.address)
packageHash.insert(package.package39.package_id, package.package39.address)
packageHash.insert(package.package40.package_id, package.package40.address)
print(packageHash.table)

'''print("\nLoopkup:")
print(packageHash.lookup(1))
print(packageHash.lookup(2))'''

