temp = [28, 32, 35, 40, 31, 33, 30]
hot_days = 0
for day in range(len(temp)):
    t = temp[day]
    if t >= 40:
        print("Hot Days before alert:", hot_days)
        print("Alert! Extreme temperature 40°C detected on Day", day + 1)
        break
    if t > 30:
        hot_days += 1