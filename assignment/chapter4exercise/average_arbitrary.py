def average(number, *args):
    total = number + sum(args)
    count = 1 + len(args)
    return total / count

print(average(10, 20, 30)) 
