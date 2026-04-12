age = int(input('Enter your age: '))


max_heart_rate = 220 - age
range_one = max_heart_rate * 0.50
range_two = max_heart_rate * 0.85


print("Maximum heart rate:", max_heart_rate)
print(range_one, ":", range_two)
