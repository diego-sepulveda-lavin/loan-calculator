halls_number = int(input())
capacity = int(input())
viewers_number = int(input())

total_capacity = capacity * halls_number
can_accommodate = viewers_number <= total_capacity

print(can_accommodate)
