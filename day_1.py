list_1 = []
list_2 = []

with open('data/day_1.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        zahl1, zahl2 = map(int, line.split())
        list_1.append(zahl1)
        list_2.append(zahl2)

list_1.sort()
list_2.sort()

sum1 = 0

for i in range(len(list_1)):
    diff = list_1[i] - list_2[i]
    if diff < 0:
        diff *= -1
    sum1 += diff

print(sum1)

sum2 = 0

for number in list_1:
    amount = list_2.count(number)
    sum2 += amount * number

print(sum2)
    

