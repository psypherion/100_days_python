ip = input("Enter the Ages (separated by spaces)").split()
sum = 0
for i in range(0,(len(ip)-1)):
  sum = sum + int(ip[i])
avg = sum/len(ip)
print(f"Average of Age: {round(avg,3)}")
