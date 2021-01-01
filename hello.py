print("Hello World, this is Captain Khalil")
print("")

balance = 1000
name = "Khalil"
account_id = "20203131"

print("Print the output using regular variables")
print("name:", name, "   account:", account_id,"    balance", "$" + str(balance))

charge1 = 20.19
charge2 = 159.9
charge3 = 200.0

balance = balance - charge1
print("name:", name, "   account:", account_id,"    charge:", charge1,"    new balance", "$" + str(balance))

balance = balance - charge2
print("name:", name, "   account:", account_id,"    charge:", charge2,"    new balance", "$" + str(balance))

balance = balance - charge3
print("name:", name, "   account:", account_id,"    charge:", charge3,"    new balance", "$" + str(balance))

print("")
print("Print the output using array of variables")
#Reset the balance to 1000
balance = 1000
print("name:", name, "   account:", account_id,"    balance", "$" + str(balance))

charges = [20.19,159.9,200.0]
balance = balance - charge1
print("name:", name, "   account:", account_id,"    charge:", charges[0],"    new balance", "$" + str(balance))

balance = balance - charge2
print("name:", name, "   account:", account_id,"    charge:", charges[1],"    new balance", "$" + str(balance))

balance = balance - charge3
print("name:", name, "   account:", account_id,"    charge:", charges[2],"    new balance", "$" + str(balance))


print("")
print("Print the output using array of variables and a while loop")
#Reset the balance to 1000
balance = 1000
print("name:", name, "   account:", account_id,"    balance", "$" + str(balance))

charges = [20.19,159.9,200.0]
for charge in charges:
    balance = balance - charge
    print("name:", name, "   account:", account_id,"    charge:", charge,"    new balance", "$" + str(balance))


print("")
print("Print the output using array of variables and a while loop for a file")
#Reset the balance to 1000
balance = 1000
print("name:", name, "   account:", account_id,"    balance", "$" + str(balance))

charges_file = open("charges")
for charge in charges_file:
    balance = balance - float(charge)
    print("name:", name, "   account:", account_id,"    charge:", charge.strip(),"    new balance", "$" + str(balance))
