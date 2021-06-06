print("Welcome to the tip calculator...")
ip = float(input("What was The total Bill? $"))
pers = int(input("How many people to split the Bill? "))
tip = int(input("What percantage tip would you like to give? 10, 12 or 15? "))
op = (ip + (ip*(tip/100)))/pers
print("Each person should pay: $",round(op,2))
