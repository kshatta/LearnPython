#!/usr/bin/env python
print ("hello world")
principla = 1000
rate = 0.05
numyears = 5
year = 1
while year <= numyears:
    principla = principla * (1+rate)
    print (year, principla)
    year += 1

print   ( 96 + 40)
print (144 - 136)

""" f = open("wc-a.costaric.txt")
line = f.readline()
while line:
    print (line),
    line = f.readline()
f.close()     """

x = "37"
y = "42"
z = x + y
print(z)

print("The value of x is " + str(x))
print("The value of x is " + repr(x))
#print("The value of x is " + "{0:.5f}".format(x))

#print("{0:.2f}".format(charge))

names = ["Dave","Mark","Ann","Phil"]

a = names[2]
print(a)

print("")
print("---People-----------------")
person_no = 1
with open('lab_people.txt','r') as people_file:
    for person in people_file:
        print(person_no, "       name:", person.strip())
        person_no += 1

print("")
print("Totale people: ",person_no-1)

charge = 5.432
print("{0:.2f}".format(charge))

balance = 100
name = "Abou Houssam"
account_no = "2349832"
print("\nName             Account      Charge    balance")
for charge in open("lab_charges.txt"):
    balance = balance - float(charge)
    print("{0:16} {1:10} {2:6,.2f} {3:10,.2f}".format(name,account_no,float(charge), float(balance)))