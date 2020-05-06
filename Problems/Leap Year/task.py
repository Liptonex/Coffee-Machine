#  Posted from EduTools plugin
year = int(input())

if year % 4 == 0:
    if not year % 100 == 0:
        print("Leap")
    if year % 400 == 0:
        print("Leap")
else:
    print("Ordinary")