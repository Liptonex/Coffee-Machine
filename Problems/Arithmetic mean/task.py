#  Posted from EduTools plugin
numbers = [int(x) for x in input().split()]
sum = 0
dev = 0
for i in numbers:
    sum += i
    dev +=1
art = sum/dev
print(art)