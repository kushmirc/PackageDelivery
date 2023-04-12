# PackageDelivery

### <em>Video Walkthrough: </em>https://youtu.be/1WIykO5yglE
<a href="https://youtu.be/1WIykO5yglE">
<img src="https://user-images.githubusercontent.com/107213928/231574545-1d219c8f-4aaf-4c91-8ebb-38237a5e0cca.png" alt="video walkthrough"></a>


## Summary:
This is a Python program built using the Pycharm IDE. The purpose of the program is to find the shortest route for delivering mail packages to different addresses.  
The scenario is based on a sample of 40 packages which are delivered to addresses around Salt Lake City, UT.  There are three trucks and two drivers available for 
delivering the packages. Each package has eight attributes including a unique package ID, a destination address, and a delivery status. This data is loaded into the
program from an Excel file which was converted to csv. Distance and address csv files are also loaded into the system to provide the data used in the scenario.

each of the five JavaFX windows. Users are able to add modify and delete part and products using buttons on the main screen. They can search for parts and products
using the search fields on the main screen. There are error handling messages presented when various invalid operations are performed by the user, as well as
confirmation dialogue boxes for deleting parts, products, and associated parts for products.  

There are five class files.  The inventory class houses the majority of the methods used for managing parts and products. Three classes, Parts, InHouse and Outsourced
are related to parts. Parts is an abstract class with two children, InHouse and Outsourced. The Products class handles all product related members.  
There are Javadocs provided in the InventorySystem directory which includes descriptions of all classes and methods. Please see the Javadocs for more detailed descriptions.  

This application was built with JavaFX SDK version 18.0.1 and JDK 17.  The IntelliJ JavaFX project generator was used with the Maven Build System selection when creating the project in IntelliJ.  Scene Builder was used for creating the UI layouts of the fxml files.