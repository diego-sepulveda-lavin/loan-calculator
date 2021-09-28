initial_atoms_qty = int(input())
final_atoms_qty = int(input())
half_life_periods = 0
half_life = 12

while final_atoms_qty <= initial_atoms_qty:
    initial_atoms_qty //= 2
    half_life_periods += 1

total_days = half_life_periods * half_life

print(total_days)
