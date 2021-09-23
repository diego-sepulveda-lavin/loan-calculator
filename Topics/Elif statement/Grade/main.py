student_score = int(input())
max_score = int(input())

obtained_percentage = student_score / max_score
a_percentage = 0.9
b_percentage = 0.8
c_percentage = 0.7
d_percentage = 0.6

if obtained_percentage >= a_percentage:
    print("A")
elif obtained_percentage >= b_percentage:
    print("B")
elif obtained_percentage >= c_percentage:
    print("C")
elif obtained_percentage >= d_percentage:
    print("D")
else:
    print("F")
