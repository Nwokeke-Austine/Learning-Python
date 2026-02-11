temps = [30, 28, 35, 40, 25]
above_30 = 0

print("Temperature: ")
for temp in temps:
    print(temp)

    if temp > 30:
        above_30 += 1

print(above_30, "temperatues are above 30")
