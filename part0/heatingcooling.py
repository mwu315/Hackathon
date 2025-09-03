heating_days = 0
cooling_days = 0

while True:
    temp = int(input("Enter the average daily temperature: "))
    if temp < -459:
        break

    if temp < 60:
        heating_days += 1
    elif temp > 80:
        cooling_days += 1

print(f"Heating days: {heating_days}")
print(f"Cooling days: {cooling_days}")
