min_sleeping_hours = int(input())  # A
max_sleeping_hours = int(input())  # B
ann_sleeping_hours = int(input())  # H

if ann_sleeping_hours > max_sleeping_hours:
    print("Excess")
elif ann_sleeping_hours < min_sleeping_hours:
    print("Deficiency")
else:
    print("Normal")
