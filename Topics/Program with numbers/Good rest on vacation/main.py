# put your python code here
duration_in_days = int(input())
daily_food_cost = int(input())
one_way_flight_cost = int(input())
hotel_cost_per_night = int(input())

total_food_cost = duration_in_days * daily_food_cost
total_flights_cost = one_way_flight_cost * 2
total_hotel_cost = (duration_in_days - 1) * hotel_cost_per_night

total_vacation_cost = total_food_cost + total_flights_cost + total_hotel_cost
print(total_vacation_cost)
