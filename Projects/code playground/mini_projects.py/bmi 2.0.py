# number = int(input("which number do you want to change"))
# # 7%2 gives us the remainder of the number
# if number % 2 == 0:
#     print("the number is even")
# else:
#      print(" the number is odd")

height = float(input("what is your height"))
weight = float(input("what is your weight"))
bmi = weight / height**2 
if bmi< 18:
    print(" you are underweight")
elif 18.5<bmi<25 :
     print ("you are of normal weight")
elif 25<bmi<30 :
     print (" you are overweight")
elif 30<bmi<35 :
     print(" you are obese")
else: 
     print (" you are clinically obese")

#this code is working put not running in python terminal