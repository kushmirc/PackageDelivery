# PackageDelivery

### <em>Video Walkthrough: </em>https://youtu.be/1WIykO5yglE
<a href="https://youtu.be/1WIykO5yglE">
<img src="https://user-images.githubusercontent.com/107213928/231574545-1d219c8f-4aaf-4c91-8ebb-38237a5e0cca.png" alt="video walkthrough"></a>


## Summary:
This is a Python program built using the Pycharm IDE. The purpose of the program is to find the shortest route for delivering mail packages to different addresses.

The scenario is based on a sample of 40 packages which are delivered to addresses around Salt Lake City, UT.  There are three trucks and two drivers available for 
delivering the packages. Each package has eight attributes including a unique package ID, a destination address, and a delivery status. This data is loaded into the
program from an Excel file which was converted to csv. Distance and address csv files are also loaded into the system to provide the data used in the scenario.

The program employs a hash table data structure to optimize package search and update time. The hash table is created as a two-dimentional list. There are ten hash buckets, each created as a list. Packages are placed into an appropriate bucket by calculating the package ID modulo ten. Collisions are handled by chaining the hash table so that multiple packages can be placed in each hash bucket.  

The program also employs a "nearest neighbor" algorithm to enable the delivery of packages to be executed in a way that minimizes the time taken and distance traveled by the delivery trucks. The algorithm works by evaluating the distance between the current address of the truck and the address of every package loaded on the truck.
The closest package is identified, and the next delivery is made to that address. The algorithm then loops back to find the next nearest package again from among those
remaining in the truck. 

There is a user input-output capability which takes place in the console. When the main.py file of the program is run, the user is presented with a menu of options.
The entire delivery program may be run with the first option, and a report is printed showing the activity accomplished by each truck. Alternatively, the user can 
check the status of all packages, or of just one package at a time chosen by the user. If the user choses an invalid option the program prints an error message, and 
waits for additional input. 
descriptions.  
