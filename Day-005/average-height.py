student_height = input("Input a list of student height ").split()
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])
print(student_height)

total_height = 0
for height in student_height:
    total_height += height
print(total_height)

number_of_height = 0
for number in student_height:
    number_of_height += 1
print(number_of_height)

average_height = round(total_height / number_of_height)
print(average_height)