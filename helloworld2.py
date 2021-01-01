""" charges_file = open("lab_charges2.txt")
for charge in charges_file:
    charge_info = charge.strip().split(',')
    print(charge_info)
 """
"""
charges_file = open("lab_charges2.txt")

charges_list = []
for charge in charges_file:
    charge_info = charge.strip().split(',')
    charges_list.append(charge_info)

#print(charges_list)    
balance = 100
for charge in charges_list:
    balance = balance - float(charge[2])
    print("{0:24} {1:10} {2:15,.2f} {3:15,.2f}".format(charge[0],charge[1],float(charge[2]),balance))
    #print(charges_list[0] + "    " + charges_list[1] + "    " + charges_list[2])
"""
"""
charges_file = open("lab_charges2.txt")

charges_list = []
for charge in charges_file:
    charge_info = charge.strip().split(',')
    charge_dict = dict()
    charge_dict['vendor'] = charge_info[0]
    charge_dict['date'] = charge_info[1]
    charge_dict['charge'] = charge_info[2]
    
    charges_list.append(charge_dict)

#print(charges_list)    
balance = 100
for charge in charges_list:
    balance = balance - float(charge['charge'])
    print("{0:24} {1:10} {2:15,.2f} {3:15,.2f}".format(charge['vendor'],charge['date'],float(charge['charge']),balance))
    #print(charges_list[0] + "    " + charges_list[1] + "    " + charges_list[2])

"""
from operator import itemgetter
charges_file = open("lab_charges2.txt")

charges_list = []
charges_dict = dict()
for charge in charges_file:
    charge_info_list = charge.strip().split(',')
    charge_info = dict()
    charge_info['vendor'] = charge_info_list[0]
    charge_info['date'] = charge_info_list[1]
    charge_info['charge'] = charge_info_list[2]
    
    charges_list.append(charge_info)

    if charge_info['vendor'] not in charges_dict:
        charges_dict[charge_info['vendor']] = list()

    charges_dict[charge_info['vendor']].append(charge_info)

charges_sorted_by_date = sorted(charges_list, key = itemgetter('date'))
#print(charges_list)
print("******************************************************************")
print("Before Sorting")    
print("******************************************************************")
balance = 200
for charge in charges_list:
    balance = balance - float(charge['charge'])
    print("{0:24} {1:10} {2:15,.2f} {3:15,.2f}".format(charge['vendor'],charge['date'],float(charge['charge']),balance))
    #print(charges_list[0] + "    " + charges_list[1] + "    " + charges_list[2])
print("******************************************************************")
print("After Sorting")
print("******************************************************************")
balance = 200
for charge in charges_sorted_by_date:
    balance = balance - float(charge['charge'])
    print("{0:24} {1:10} {2:15,.2f} {3:15,.2f}".format(charge['vendor'],charge['date'],float(charge['charge']),balance))
    #print(charges_list[0] + "    " + charges_list[1] + "    " + charges_list[2])
print("******************************************************************")
print("Combine by Vendor")
print("******************************************************************")
balance = 200
for vendor, charge_info_list in charges_dict.items():
    for charge_info in charge_info_list:
        balance = balance - float(charge_info['charge'])
        print("{0:24} {1:10} {2:15,.2f} {3:15,.2f}".format(charge_info['vendor'],charge_info['date'],float(charge_info['charge']),balance))
    print("------")    

while True:
    vendor_to_find = input('\n\nEnter vendor to find:   ')
    if len(vendor_to_find) == 0:
        break

    if vendor_to_find not in charges_dict:
        print('vendor {} not found'.format(vendor_to_find))
        continue

    print("\n")
    for charge_info in charges_dict[vendor_to_find]:
        print("{0:24} {1:10} {2:15,.2f} {3:15,.2f}".format(charge_info['vendor'],charge_info['date'],float(charge_info['charge']),balance))
    
print('Good bye')
exit()