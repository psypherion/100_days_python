# exercise - 2
# Banker roulette
import random
ip = int(input("how many people are here?"))
name = []
for i in range (0,ip):
  nam = input("Name of peoples:")
  name.append(nam)
  i+= 1
ran = random.randint(0,ip)
s = name[ran]
print(f"{s} will pay the bill.")
