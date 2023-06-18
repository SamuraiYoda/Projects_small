
age = input("what is your age ")
age_as_int = int(age)
years_left = float (90 - age_as_int)
months_left = float(years_left *12)
days_left = float(years_left * 365)
weeks_left = years_left* 52
message = f" you have {years_left} years, {months_left} months  , {weeks_left} weeks  {days_left} days left to live" 
print(message)