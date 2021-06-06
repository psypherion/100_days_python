ter = False
new = {}
ar = []
while ter == False :
  name = input("Enter Your Name : ")
  bid = int(input("Enter your Bidding Price : "))
  new[name] = bid
  others = input("Is ther any other Bidders ? Type Yes/No ").lower()
  if others == "no" :
    ter = True
  elif others == "yes" :
    ter = ter
for i in new :
  ar.append(new.get(i))
for i in new:
  if new.get(i) == max(ar) :
    print(f"The Winner of The Bidding Is : {i}")
