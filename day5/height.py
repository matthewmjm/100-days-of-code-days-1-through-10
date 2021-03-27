# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)

# 180 124 165 173 189 169 146

# can not use
# population = len(student_heights)
# tally =  sum(student_heights) 

i = 0
sum = 0

student_heights = input("Input a list of student heights ").split()
for student in student_heights:
    i += 1
    sum += int(student)
average = round(sum/i)
print(f"The average student height is {average}.")
