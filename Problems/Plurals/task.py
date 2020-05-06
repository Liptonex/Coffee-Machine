#  Posted from EduTools plugin
number = int(input())
word = input()

# write a condition for plurals

if number >= 2:
    print(number, word + "s")
elif number == 0:
    print(number, word + "s")
else:
    print(number, word)

