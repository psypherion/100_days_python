# exercise-2
# Highest Score:
ip = input("Enter The scores : ").split()
ip_1 = []
for i in range(0,(len(ip)-1)):
  ip_1.append(int(ip[i]))
print(max(ip))
