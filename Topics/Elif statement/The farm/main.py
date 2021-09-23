chicken_price = 23
goat_price = 678
pig_price = 1296
cow_price = 3848
sheep_price = 6769

user_money_amount = int(input())

can_buy_sheep = user_money_amount >= sheep_price
can_buy_cow = user_money_amount >= cow_price
can_buy_pig = user_money_amount >= pig_price
can_buy_goat = user_money_amount >= goat_price
can_buy_chicken = user_money_amount >= chicken_price

if can_buy_sheep:
    sheep_amount = user_money_amount // sheep_price
    print(sheep_amount, "sheep")

elif can_buy_cow:
    cow_amount = user_money_amount // cow_price
    print(cow_amount, "cows" if cow_amount > 1 else "cow")

elif can_buy_pig:
    pig_amount = user_money_amount // pig_price
    print(pig_amount, "pigs" if pig_amount > 1 else "pig")

elif can_buy_goat:
    goat_amount = user_money_amount // goat_price
    print(goat_amount, "goats" if goat_amount > 1 else "goat")

elif can_buy_chicken:
    chicken_amount = user_money_amount // chicken_price
    print(chicken_amount, "chickens" if chicken_amount > 1 else "chicken")

else:
    print("None")
