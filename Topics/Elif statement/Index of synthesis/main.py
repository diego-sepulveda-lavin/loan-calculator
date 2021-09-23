synthesis_index = float(input())
polysynthetic_index = 3
synthetic_index = 2

if synthesis_index > polysynthetic_index:
    print("Polysynthetic")
elif synthesis_index >= synthetic_index:
    print("Synthetic")
else:
    print("Analytic")
