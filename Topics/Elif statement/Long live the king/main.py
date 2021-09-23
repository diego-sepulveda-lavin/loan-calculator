col_pos = int(input())
row_pos = int(input())

col_limits = [1, 8]
row_limits = [1, 8]

is_at_corner = (col_pos in col_limits) and (row_pos in row_limits)
is_at_edge = (col_pos in col_limits) or (row_pos in row_limits)

max_moves = 8

if is_at_corner:
    max_moves = 3
elif is_at_edge:
    max_moves = 5

print(max_moves)
