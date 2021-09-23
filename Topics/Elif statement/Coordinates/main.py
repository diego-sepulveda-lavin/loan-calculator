x_pos = float(input())
y_pos = float(input())

is_x_positive = x_pos > 0
is_y_positive = y_pos > 0

if x_pos == 0 and y_pos == 0:
    print("It's the origin!")
elif x_pos == 0 or y_pos == 0:
    print("One of the coordinates is equal to zero!")
elif is_x_positive:
    if is_y_positive:
        print("I")
    else:
        print("IV")
elif not is_x_positive:
    if is_y_positive:
        print("II")
    else:
        print("III")
