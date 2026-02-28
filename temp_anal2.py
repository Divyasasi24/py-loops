temp = [28, 32, 35, 29, 31, 27, 30]
hot_days = 0
for t in temp:
    if t <= 30:
        continue   
    hot_days += 1
print("Hot Days:", hot_days)