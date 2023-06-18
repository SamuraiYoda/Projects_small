def add(n1, n2):
  return n1 + n2

def multiply(n1 , n2):
  return n1 * n2

def divide(n1,n2):
  return n1/n2

def sub(n1, n2):
  return n1 - n2

operations = {
  
   "+":  add ,
  "-" : sub,
   "*": multiply,
   "/" : divide 

}
# function = operation["+"]
def calculator():
  num1 = int(input("what is your first number? "))
  for symbol in operations:
    print(symbol)
  should_continue = True
  
  while should_continue:
    operation_symbol = input("pick an operation from the line above ")
    calculation_function = operations[operation_symbol]
    num2 = int(input("what is your next number? "))
    answer = calculation_function(num1, num2)
  
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    if input(f"would you like to continue with {answer} if yes then type 'y' else 'n'") == "y":
      num1 = answer
    else:
      should_continue = False
      calculator()# this call function works as recursion, calling the function 
  
    
calculator()    #this is where we start the program by calling the calculator() function
                # single =  is used for boolean True or False
                # single ' ' is used for input value for 'y' yes and 'n' no
                # in dictionary to use function from key operation[operation_symbol] is used-
                # to fetch value and execute the function
                # recursion- calculator is used in else to call the function to restart the code
