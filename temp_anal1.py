temp = [28, 32, 35, 29, 31, 27, 30]
high = temp[0]
low = temp[0]
for t in temp:
    if t > high:
        high = t
    if t < low:
        low = t
print("Highest Temperature:", high, "°C")
print("Lowest Temperature:", low, "°C")