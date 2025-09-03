speed_limit = float(input('Enter the speed limit:'))
driving_speed = float(input('Enter the driving speed:'))
difference = driving_speed - speed_limit

if difference > 40:
    print("300")
elif 21 <= difference <= 40:
    print("150")
elif 6 <= difference <= 20:
    print("75")
elif difference <= -10:
    print("50")
else:
    print("0")
print("bye")
