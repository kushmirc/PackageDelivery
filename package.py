#Read packageCSV file and create a 2d list of packages
#space-time complexity: O(8N)
import csv

with open("packageCSV.csv", encoding='utf-8-sig') as fp:
    reader = csv.reader(fp, delimiter=",", quotechar='"' )
    package_list = [row for row in reader]

#Create the Package class with a constructor containing all package fields from the packageCSV
class Package:
    def __init__(self, package_id, address, city, state, zip, delivery_deadline, weight, special_notes, delivery_status):
        self.package_id = int(package_id)
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.delivery_deadline = delivery_deadline
        self.weight = weight
        self.special_notes = special_notes
        self.delivery_status = delivery_status

#Create all package objects.
#space-time complexity: 40(O(8))
package1 = Package(package_list[0][0],package_list[0][1],package_list[0][2],package_list[0][3],package_list[0][4],package_list[0][5],package_list[0][6],package_list[0][7],'at the hub')

package2 = Package(package_list[1][0], package_list[1][1], package_list[1][2], package_list[1][3], package_list[1][4], package_list[1][5], package_list[1][6], package_list[1][7],'at the hub')

package3 = Package(package_list[2][0], package_list[2][1], package_list[2][2], package_list[2][3], package_list[2][4], package_list[2][5], package_list[2][6], package_list[2][7],'at the hub')

package4 = Package(package_list[3][0], package_list[3][1], package_list[3][2], package_list[3][3], package_list[3][4], package_list[3][5], package_list[3][6], package_list[3][7],'at the hub')

package5 = Package(package_list[4][0], package_list[4][1], package_list[4][2], package_list[4][3], package_list[4][4], package_list[4][5], package_list[4][6], package_list[4][7],'at the hub')

package6 = Package(package_list[5][0], package_list[5][1], package_list[5][2], package_list[5][3], package_list[5][4], package_list[5][5], package_list[5][6], package_list[5][7],'at the hub')

package7 = Package(package_list[6][0], package_list[6][1], package_list[6][2], package_list[6][3], package_list[6][4], package_list[6][5], package_list[6][6], package_list[6][7],'at the hub')

package8 = Package(package_list[7][0], package_list[7][1], package_list[7][2], package_list[7][3], package_list[7][4], package_list[7][5], package_list[7][6], package_list[7][7],'at the hub')

package9 = Package(package_list[8][0], package_list[8][1], package_list[8][2], package_list[8][3], package_list[8][4], package_list[8][5], package_list[8][6], package_list[8][7],'at the hub')

package10 = Package(package_list[9][0], package_list[9][1], package_list[9][2], package_list[9][3], package_list[9][4], package_list[9][5], package_list[9][6], package_list[9][7],'at the hub')

package11 = Package(package_list[10][0], package_list[10][1], package_list[10][2], package_list[10][3], package_list[10][4], package_list[10][5], package_list[10][6], package_list[10][7],'at the hub')

package12 = Package(package_list[11][0], package_list[11][1], package_list[11][2], package_list[11][3], package_list[11][4], package_list[11][5], package_list[11][6], package_list[11][7],'at the hub')

package13 = Package(package_list[12][0], package_list[12][1], package_list[12][2], package_list[12][3], package_list[12][4], package_list[12][5], package_list[12][6], package_list[12][7],'at the hub')

package14 = Package(package_list[13][0], package_list[13][1], package_list[13][2], package_list[13][3], package_list[13][4], package_list[13][5], package_list[13][6], package_list[13][7],'at the hub')

package15 = Package(package_list[14][0], package_list[14][1], package_list[14][2], package_list[14][3], package_list[14][4], package_list[14][5], package_list[14][6], package_list[14][7],'at the hub')

package16 = Package(package_list[15][0], package_list[15][1], package_list[15][2], package_list[15][3], package_list[15][4], package_list[15][5], package_list[15][6], package_list[15][7],'at the hub')

package17 = Package(package_list[16][0], package_list[16][1], package_list[16][2], package_list[16][3], package_list[16][4], package_list[16][5], package_list[16][6], package_list[16][7],'at the hub')

package18 = Package(package_list[17][0], package_list[17][1], package_list[17][2], package_list[17][3], package_list[17][4], package_list[17][5], package_list[17][6], package_list[17][7],'at the hub')

package19 = Package(package_list[18][0], package_list[18][1], package_list[18][2], package_list[18][3], package_list[18][4], package_list[18][5], package_list[18][6], package_list[18][7],'at the hub')

package20 = Package(package_list[19][0], package_list[19][1], package_list[19][2], package_list[19][3], package_list[19][4], package_list[19][5], package_list[19][6], package_list[19][7],'at the hub')

package21 = Package(package_list[20][0], package_list[20][1], package_list[20][2], package_list[20][3], package_list[20][4], package_list[20][5], package_list[20][6], package_list[20][7],'at the hub')

package22 = Package(package_list[21][0], package_list[21][1], package_list[21][2], package_list[21][3], package_list[21][4], package_list[21][5], package_list[21][6], package_list[21][7],'at the hub')

package23 = Package(package_list[22][0], package_list[22][1], package_list[22][2], package_list[22][3], package_list[22][4], package_list[22][5], package_list[22][6], package_list[22][7],'at the hub')

package24 = Package(package_list[23][0], package_list[23][1], package_list[23][2], package_list[23][3], package_list[23][4], package_list[23][5], package_list[23][6], package_list[23][7],'at the hub')

package25 = Package(package_list[24][0], package_list[24][1], package_list[24][2], package_list[24][3], package_list[24][4], package_list[24][5], package_list[24][6], package_list[24][7],'at the hub')

package26 = Package(package_list[25][0], package_list[25][1], package_list[25][2], package_list[25][3], package_list[25][4], package_list[25][5], package_list[25][6], package_list[25][7],'at the hub')

package27 = Package(package_list[26][0], package_list[26][1], package_list[26][2], package_list[26][3], package_list[26][4], package_list[26][5], package_list[26][6], package_list[26][7],'at the hub')

package28 = Package(package_list[27][0], package_list[27][1], package_list[27][2], package_list[27][3], package_list[27][4], package_list[27][5], package_list[27][6], package_list[27][7],'at the hub')

package29 = Package(package_list[28][0], package_list[28][1], package_list[28][2], package_list[28][3], package_list[28][4], package_list[28][5], package_list[28][6], package_list[28][7],'at the hub')

package30 = Package(package_list[29][0], package_list[29][1], package_list[29][2], package_list[29][3], package_list[29][4], package_list[29][5], package_list[29][6], package_list[29][7],'at the hub')

package31 = Package(package_list[30][0], package_list[30][1], package_list[30][2], package_list[30][3], package_list[30][4], package_list[30][5], package_list[30][6], package_list[30][7],'at the hub')

package32 = Package(package_list[31][0], package_list[31][1], package_list[31][2], package_list[31][3], package_list[31][4], package_list[31][5], package_list[31][6], package_list[31][7],'at the hub')

package33 = Package(package_list[32][0], package_list[32][1], package_list[32][2], package_list[32][3], package_list[32][4], package_list[32][5], package_list[32][6], package_list[32][7],'at the hub')

package34 = Package(package_list[33][0], package_list[33][1], package_list[33][2], package_list[33][3], package_list[33][4], package_list[33][5], package_list[33][6], package_list[33][7],'at the hub')

package35 = Package(package_list[34][0], package_list[34][1], package_list[34][2], package_list[34][3], package_list[34][4], package_list[34][5], package_list[34][6], package_list[34][7],'at the hub')

package36 = Package(package_list[35][0], package_list[35][1], package_list[35][2], package_list[35][3], package_list[35][4], package_list[35][5], package_list[35][6], package_list[35][7],'at the hub')

package37 = Package(package_list[36][0], package_list[36][1], package_list[36][2], package_list[36][3], package_list[36][4], package_list[36][5], package_list[36][6], package_list[36][7],'at the hub')

package38 = Package(package_list[37][0], package_list[37][1], package_list[37][2], package_list[37][3], package_list[37][4], package_list[37][5], package_list[37][6], package_list[37][7],'at the hub')

package39 = Package(package_list[38][0], package_list[38][1], package_list[38][2], package_list[38][3], package_list[38][4], package_list[38][5], package_list[38][6], package_list[38][7],'at the hub')

package40 = Package(package_list[39][0], package_list[39][1], package_list[39][2], package_list[39][3], package_list[39][4], package_list[39][5], package_list[39][6], package_list[39][7],'at the hub')

