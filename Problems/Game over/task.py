#  Posted from EduTools plugin
scores = input().split()
incorrect = []
correct = []

while True:
    # print("First loop")
    for i in scores:
        # print("Second loop")
        if i == "C":
            # print("Correct")
            correct.append(i)
        elif i == "I":
            # print("Incorrect")
            incorrect.append(i)
        if len(incorrect) == 3:
            print("Game over")
            print(len(correct))
            break
    if len(incorrect) == 3:
        break
    print("You won")
    print(len(correct))
    break



