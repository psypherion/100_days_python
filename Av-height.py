# exercise-1 
# Average Height :
ip = int(input("Enter number of people :"))
sum = 0
for i in range (0,ip):
  age = int(input("Enter Age : "))
  sum += age
avg = sum/ip
print(f"Average Height is: {avg} ")
