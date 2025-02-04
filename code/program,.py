'''
This is the main program. 
You should read the packaging.txt in the data folder.
Each line contains one package description. 
You should parse the package description using parse_packaging()
print the total number of items in the package using calc_total_units()
along with the unit using get_unit()
place each package in a list and save in JSON format.

Example:

    INPUT (example data/packaging.txt file):
    
    12 eggs in 1 carton
    6 bars in 1 pack / 12 packs in 1 carton

    OUTPUT: (print to console)

    12 eggs in 1 carton => total units: 12 eggs
    6 bars in 1 pack / 12 packs in 1 carton => total units: 72 bars

    OUTPUT (example data/packaging.json file):
    [
        [{ 'eggs' : 12}, {'carton' : 1}],
        [{ 'bars' : 6}, {'packs' : 12}, {'carton' : 1}],
    ]    
'''

# TODO: Write code

import json
packages = [] # Empty list to add parsed line data to

# Parsing text file 
from packaging import parse_packaging, calc_total_units, get_unit

with open("data/packaging.txt", "r") as file:
    for line in file.readlines():
        package_list = parse_packaging(line) # Create new list after parsing line
        total_items = calc_total_units(package_list)
        unit = get_unit(package_list)
        print(f"{line} => total units: {total_items} {unit}") # print output
        packages.append(package_list) # Adding package_list to greater list of packages, for json output


        # Sending data to json file
        with open("data/packaging.json", "w") as j:
            json.dump(packages, j, indent = 4)




