# OBESITY CALCULATOR
weight = float(input("what is your weight ?"))
height = float(input("what is your height ?"))

BMI = (weight/(height**2))

print (BMI)

if BMI > 40:
    print ("OBESE")
elif BMI > 25 : 
    print ("OVERWEIGHT")
elif BMI > 18 :
    print ("NORMAL")
else :
    print ("UNDERWEIGHT")
