threshold = float(input())
n = int(input())

errors = 0
above = 0
count = 0
total = 0
max_temp = 0

for i in range(n):
    line = input().strip()

    if line == "error":
        errors += 1
    else:
        temp = float(line)

        if temp > threshold:
            above += 1

        if count == 0 or temp > max_temp:
            max_temp = temp

        total += temp
        count += 1

print(n)
print(errors)
print(above)
print(f"{max_temp:.1f}")
print(f"{total / count:.1f}")
