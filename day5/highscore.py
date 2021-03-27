# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores


# 78 65 89 86 55 91 64 89

student_scores = input("Input a list of student scores ").split()
highest_score = 0
print(student_scores)
for score in student_scores:
    print(int(score))
    if highest_score > int(score):
        highest_score = highest_score
    else:
        highest_score = int(score)
print(f"The highest score in the class is: {highest_score}")