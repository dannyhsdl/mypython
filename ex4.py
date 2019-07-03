#coding=utf-8
#'cars' here is a variable.
cars=100 # '=' here is equal,it is used to name something which we got.
space_in_a_car=4.0 # '_' here is underscore.
drivers=30
passengers=90
cars_not_driven=cars-drivers #Tell people how many cars here which are not driven.

cars_driven=drivers
carpool_capacity=cars_driven*space_in_a_car
average_passengers_per_car=passengers/cars_driven


print("There are",cars,"cars available.") # To tell people how many car here are available.
print("There are only",drivers,"drivers available.")
print("There will be",cars_not_driven,"empty cars today.")
print("We can transport",carpool_capacity,"people today.")
print("We have",passengers,"to carpool today.")
print("We need to put about",average_passengers_per_car,"in each car.")
