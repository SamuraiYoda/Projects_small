year = int(input("which year do you want to check"))

if year % 4 == 0:
    if year %100 == 0:
        if year % 400 == 0:
            print("this is an leap year")
        else:
            print ("this is not a leap year")
    else :
        print("this is  a leap year")
else:
    print("this is not a leap year")


#this works on making a flow chart and then using indented if else 
# function not elif function on top of each other to gather the information
