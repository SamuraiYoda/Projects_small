# # += is function used to add the value into the variable
# size = input("what size of pizza do you want S M L")
# add_pepperoni = input("do you want pepperoni Y, N")
# extra_cheese = input ("do you want extra cheese Y,N ")
# bill = 0
# if size == "s":
#     bill +=15
#     print (f" your bill is $15 ")
#     if add_pepperoni == "Y":
#         bill += 1
#         print (f"Your bill is {bill}")
#         if extra_cheese == "Y":
#             bill += 1
#             print (f"Your bill is {bill}")
#         else:
#             bill =16
#             print (f"Your bill is {bill}")
#     else:
#         bill = 15
#         print (f" Your bill is {bill}")
# elif size == "m":
#     bill =20
#     print (f" your bill is $20")

#     if add_pepperoni == "Y":
#         bill += 2
#         print (f"Your bill is {bill}") 
#         if extra_cheese == "Y":
#             bill += 1
#             print (f"Your bill is {bill}")  
#         else:
#             bill = 22
#             print (f"your bill is {bill}")
#     else:
#         bill =22
#         print (f"your bill is {bill}")
# elif size == "l":
#     bill = 25
#     print (f" your bill is $25")

#     if add_pepperoni == "Y":
#         bill += 2
#         print (f"Your bill is {bill}")
#         if extra_cheese == "Y":
#             bill += 1
#             print (f"Your bill is {bill}")  
#         else:
#             bill = 27
#             print (f"your bill is {bill}")
#     else:
#         bill =25
#         print (f"your bill is {bill}")

    
size = input("what size of pizza do you want S M L")
add_pepperoni = input("do you want pepperoni Y, N")
extra_cheese = input ("do you want extra cheese Y,N ")
bill = 0
if size == "s":
    bill +=15
    print (f" your bill is {bill} ")
elif size == "l":
    bill += 25 
    print(f" your bill is {bill} ")
elif size == "m":
    bill += 20 
    print(f" your bill is {bill} ")

if add_pepperoni =="Y":
    if size == "s":
        bill += 1
        print(f" your bill is {bill} ")

    else:
        bill += 2
        print(f" your bill is {bill} ")

if extra_cheese =="Y":
    bill += 1   
    print(f" your bill is {bill} ")

