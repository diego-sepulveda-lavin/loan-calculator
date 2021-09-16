# put your python code here
students_qty_1 = int(input())
students_qty_2 = int(input())
students_qty_3 = int(input())

min_desktop_amount_1 = students_qty_1 // 2 + students_qty_1 % 2
min_desktop_amount_2 = students_qty_2 // 2 + students_qty_2 % 2
min_desktop_amount_3 = students_qty_3 // 2 + students_qty_3 % 2

print(min_desktop_amount_1 + min_desktop_amount_2 + min_desktop_amount_3)
