# exercise - 2
# BMI CALCULATOR :
h = float(input("Enter your height in m:"))
w = float(input("Enter your Weght in kg:"))
bmi = w/(h**2) 
if bmi < 18.5 :
  print("underweight")
elif bmi>18.5 and bmi<25 :
  print("normal weight")
elif bmi>25 and bmi<30 :
  print("overweight")
elif bmi>30 and bmi<35 :
  print("obese")
elif bmi>35 :
  print("clinically obese")
