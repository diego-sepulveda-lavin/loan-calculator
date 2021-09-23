unit_qty = int(input())

legion = 1000
swarm = 500
horde = 50
pack = 10
few = 1

if unit_qty >= legion:
    print("legion")
elif unit_qty >= swarm:
    print("swarm")
elif unit_qty >= horde:
    print("horde")
elif unit_qty >= pack:
    print("pack")
elif unit_qty >= few:
    print("few")
else:
    print("no army")
