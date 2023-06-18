# if no. / by 3 - fizz
# if no. / by 5 - buzz
#  if no. / by 15 - fizzbuzz


for number in range (1,100):
    if number % 3==0 and 5  == 0:
        print("fizzbuzz")
    elif number % 5 ==0:
        print ("buzz")
    elif number % 3  ==0:
        print ("fizz")
    else:
        print (number)


