# # creating a dictionary
# inventory = {
#     "Tomatoes":{"stock":150, "price_per_unit": 5.0},
#     "Onions":{"stock": 80, "price_per_unit": 3.5},
#     "Garden Eggs":{"stock":200, "price_per_unit": 1.0}
#  }

# print(inventory)
# print(len(inventory))
# print(type(inventory))

# transactions = 0

# while True:
#     item = input("Enter item name to purchase (Tomatoes, Onions, Garden Eggs) or 'exit': ")

#     if item.lower() == "exit":
#         print("Closing sales. Total transactions completed.")
#         break

#     if item not in inventory:
#         print("Item not found in stock. Check spelling.")
#     else:
#         quantity = int(input("Enter quantity to buy: "))

#         available_stock = inventory[item]["stock"]
#         price = inventory[item]["price_per_unit"]

#         if quantity > available_stock:
#             print(f"Sorry, only {available_stock} units of {item} remaining.")
#         else:
#             cost = quantity * price
#             inventory[item]["stock"] -= quantity
#             transactions += 1

#             print(
#                 f"Sale successful! Cost: GHS {round(cost, 2)}. "
#                 f"{inventory[item]['stock']} units of {item} remaining."
#             )


# consumption = float(input("Total water consumption for the month (in cubic meters): "))

# service_charge = 15.00
# consumption_cost = 0

# if consumption <= 15:
#     consumption_cost = consumption * 0.90
# elif consumption <= 30:
#     consumption_cost = (15 * 0.90) + ((consumption - 15) * 1.20)
# else:
#     consumption_cost = (15 * 0.90) + (15 * 1.20) + ((consumption - 30) * 1.80)

# total_bill = service_charge + consumption_cost

# print("--- Monthly Water Bill Summary ---")
# print(f"Consumption: {consumption} m3")
# print("Service Charge: GHS 15.00")
# print(f"Consumption Cost: GHS {round(consumption_cost, 2)}")
# print(f"Total Bill: GHS {round(total_bill, 2)}")

recorded_speeds = [95, 110, 100, 85, 125, 90, 105, 115, 70, 130, 99, 101, 88]
SPEED_LIMIT = 100

speeding_violations = []
total_speed = 0

for speed in recorded_speeds:
    total_speed += speed
    if speed > SPEED_LIMIT:
        print(f"WARNING: Vehicle recorded at {speed} km/h. Exceeded limit of {SPEED_LIMIT} km/h.")
        speeding_violations.append(speed)

total_vehicles = len(recorded_speeds)
total_violations = len(speeding_violations)
percentage_speeding = (total_violations / total_vehicles) * 100
average_speed = total_speed / total_vehicles

print("\n--- Traffic Speed Analysis Summary ---")
print(f"Total vehicles recorded: {total_vehicles}")
print(f"Total speeding violations: {total_violations}")
print(f"Percentage speeding: {round(percentage_speeding, 2)}%")
print(f"Average speed: {round(average_speed, 2)} km/h")

focused_speeds = recorded_speeds[2:8]
print(f"Speeds for focused inspection segment (3rd to 8th vehicle): {focused_speeds}")