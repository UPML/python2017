number = int(input())

sumOfDelimeters = 0
for i in range(1, number):
    if number % i == 0:
        sumOfDelimeters += i
print("YES" if sumOfDelimeters == number else "NO")
