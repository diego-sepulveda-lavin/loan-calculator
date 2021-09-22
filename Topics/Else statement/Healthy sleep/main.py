min_sleeping_hours = int(input())  # A
max_sleeping_hours = int(input())  # B
curr_sleeping_hours = int(input())  # H

if min_sleeping_hours <= curr_sleeping_hours <= max_sleeping_hours:
    print("Normal")
else:
    if curr_sleeping_hours < min_sleeping_hours:
        print("Deficiency")
    else:
        print("Excess")
