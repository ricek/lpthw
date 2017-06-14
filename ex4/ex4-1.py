# Write comments above each of the variable assignments

# An integer value of 100 assigned to the variable named cars
cars = 100
# A floating point number for space in a car
space_in_a_car = 4.0
# Integer, number of drivers available
drivers = 30
# Integer, number of passengers
passengers = 90
# Integer, number of cars without drivers
cars_not_driven = cars - drivers
# Integer, number of cars with drivers
cars_driven = drivers
# Float, number of maximum spaces
carpool_capacity = cars_driven * space_in_a_car
# Integer, number of average passengers that should go in per car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
      "in each car.")
