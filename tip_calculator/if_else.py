print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("you can ride the rollercoaster!!!!")
    age = int(input("what is your age? "))
    if age < 12 :
        print("please pay R5")
    elif age > 12 and age < 18:
            print("please pay R7")
    else:
        print("please pay R12")

else:
    print("Sorry, you have to grow taller before you can ride")

weight = 85
height = 1.85

bmi = weight/ (height**2)
print("your bmi is:", bmi)
if bmi < 18.5:
     print("underweight")
elif bmi >=18.5 and bmi < 25:
     print("normal weight")
else:
     print("overweight")