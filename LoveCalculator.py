# exercise - 5
# Love calculator
# use lower(), count()
n1 = input("Enter ur name: ").lower()
n2 = input("Enter his/her name: ").lower()
sdf = n1 +n2
ar = ["t","r","u","e","l","o","v","e"]
t = sdf.count("t")
r = sdf.count("r")
u = sdf.count("u")
e = sdf.count("e")
tr = t+r+u+e
l = sdf.count("l")
o = sdf.count("o")
v = sdf.count("v")
e = sdf.count("e")
lo = l+v+o+e
score = tr*10 +lo
print(score)
