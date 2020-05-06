#  Posted from EduTools plugin
n = int(input())
c = 0
list = []
while c != n:
    num = int(input())
    list.append(num)
    c += 1
sum = 0
for i in list:
    sum += i
art = sum/n

print(art)
