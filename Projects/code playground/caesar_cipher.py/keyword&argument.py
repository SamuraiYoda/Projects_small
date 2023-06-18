# # Review: 
# # Create a function called greet(). 
# # Write 3 print statements inside the function.
# # Call the greet() function and run your code.

# def greet():
#   print("hello")
#   print("hakuna matata")
#   print("yahooo!")

# greet()

# def greet_new(name):
#   print(f"hello {name}")
#   print(f"how are you {name}")

# greet_new("oscar isaac")
def greet_with_new(name, location):
  print(f"how are you {name}")
  print(f"how iś your country {location}")

greet_with_new("yogesh", "india")

# parameter= name and location
# argument is values give - yogesh and location
# position of argument in function matters
# keyword argument

greet_with_new(location="india", name="yogesh")# keyword argument

