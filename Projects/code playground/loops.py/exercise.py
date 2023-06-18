# # average student height
# # 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆


# #Write your code below this row 👇

# total_height = 0
# for height in student_heights:
#   total_height+= height
# # print (total_height)


# total_number = 0
# for number in student_heights:
#   total_number += 1
# # print (total_number)

# average_height = total_height / total_number
# print (average_height)
total =0
for number in range(2,101,2):
   total += number
print(total)

total1 = 0
for number in range (1,101):
   if number % 2 == 0:
      total1 += number

print (total1)
