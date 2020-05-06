#  Posted from EduTools plugin
sth = input()
numbers = []
while (sth != "."):
    numbers.append(int(sth))
    # print("you typed:", sth)
    # print(sth == ".")
    # print("I remember:", numbers)
    sth = input()
sum = 0
for i in numbers:
    sum += i
art = sum / len(numbers)
print(art)
