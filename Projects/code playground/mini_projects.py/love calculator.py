print  ("welcome to love calculator")
name1 = input("what is your name? \n")
name2 = input("what is their name? \n")
# using these function lower function - "angela.lower("a")"
#"angela.count("a")"
combined_str = name1 + name2 
lower_case_str = combined_str.lower()

# count1 = lower_case_str.count("t"and "r"and "u"and "e")

# count2 = lower_case_str.count("l"and "o"and "v"and "e")

# score = count1 + count2
# i made same mistake as earlier i used and operatoor to contatenate
# i should use + operator to contanate
t = lower_case_str.count("t")
r = lower_case_str.count("t")
u = lower_case_str.count("t")
e = lower_case_str.count("t")
true = t+r+u+e

l = lower_case_str.count("t")
o = lower_case_str.count("t")
v = lower_case_str.count("t")
e = lower_case_str.count("t")
love = l+o+v+e

score = str(true) + str(love)
if (score>="90") or (score<="10"):
    print(f"your score is {score} you are like glue and mentos")
elif ("40"<=score) or (score<="50"):
    print(f"your score is {score} you are alaright together ")
else:
    print(f"your score is {score}")
