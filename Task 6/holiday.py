print("Options: ")
print("A: London")
print("B: Leeds")
print("C: Manchester")
city_flight = input("Enter which city you are flying to. ")
num_nights = int(input("Enter the number of nights you will be staying at the hotel. "))
rental_days = int(input("Enter the number of days for which you will be hiring a car. "))

def hotel_cost(num_nights):
    price_per_night = 60
    return num_nights * price_per_night

def plane_cost(city_flight):
    if city_flight == "A" or city_flight == "a" :
        return 30
    elif  city_flight == "B" or city_flight == "b":
        return 40
    elif  city_flight == "C" or city_flight == "c":
        return 50
    else:
        return "Invalid flight. "
    
def car_rental(rental_days):
    daily_rental_cost = 35
    total_cost = rental_days * daily_rental_cost
    return total_cost

def holiday_cost(city_flight, num_nights, rental_days):
    total_cost = hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)
    return total_cost

print(f"Hotel Cost: {hotel_cost(num_nights)} ")
print(f"Plane Cost: {plane_cost(city_flight)} ")
print(f"Car Rental Cost: {car_rental(rental_days)} ")
print(f"Total Holiday Cost: {holiday_cost(city_flight, num_nights, rental_days)} ")