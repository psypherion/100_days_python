# exercise - 4 
# pizza order
print('''
Small Pizza : $15
Medium Pizza : $20
Large Pizza : $25
     ''')
size = input("Enter the size of your pizza s, m, l? ")
s, m, l, bill = 15, 20, 25, 0
ap = input("Do u want to Add pepperoni? for +$2 ").lower()
ec = input("Do u want to Add extra cheesee? for +$3 ").lower()
if size == "s":
  bill+=s
elif size == "m":
  bill+=m
elif size == "l":
  bill+=l
if ap == "yes" :
  bill+=2
if ec == "yes":
  bill+=3
print(bill)
