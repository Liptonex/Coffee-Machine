class CoffeMachine:
    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money
        pass

    def buy(self, opt):
        if opt == "1":
            water1 = 250
            beans1 = 16
            cups1 = 1
            while True:
                if water1 > self.water:
                    print("Sorry, not enough water!")
                    break
                if beans1 > self.beans:
                    print("Sorry, not enough coffee beans!")
                    break
                if cups1 > self.cups:
                    print("Sorry, not enough cups!")
                    break
                self.water -= water1
                self.beans -= beans1
                self.cups -= cups1
                self.money += 4
                print("I have enough resources, making you a coffee!")
                break

        elif opt == "2":
            water2 = 350
            milk2 = 75
            beans2 = 20
            cups2 = 1
            # money += 7
            while True:
                if water2 > self.water:
                    print("Sorry, not enough water!")
                    break
                if beans2 > self.beans:
                    print("Sorry, not enough coffee beans!")
                    break
                if cups2 > self.cups:
                    print("Sorry, not enough cups!")
                    break
                if milk2 > self.milk:
                    print("Sorry, not enough milk!")
                    break
                self.water -= water2
                self.beans -= beans2
                self.milk -= milk2
                self.cups -= cups2
                self.money += 7
                print("I have enough resources, making you a coffee!")
                break
        elif opt == "3":
            water3 = 200
            milk3 = 100
            beans3 = 12
            cups3 = 1
            # money += 6
            while True:
                if water3 > self.water:
                    print("Sorry, not enough water!")
                    break
                if beans3 > self.beans:
                    print("Sorry, not enough coffee beans!")
                    break
                if cups3 > self.cups:
                    print("Sorry, not enough cups!")
                    break
                if milk3 > self.milk:
                    print("Sorry, not enough milk!")
                    break
                self.water -= water3
                self.beans -= beans3
                self.cups -= cups3
                self.milk -= milk3
                self.money += 6
                print("I have enough resources, making you a coffee!")
                break
        pass

    def state(self):
        print("The coffee machine has:")
        print(self.water, "of water")
        print(self.milk, "of milk")
        print(self.beans, "of coffee beans")
        print(self.cups, "of disposable cups")
        print("$" + str(self.money), "of money")
        pass

    def fill(self):
        print("Write how many ml of water do you want to add:")
        x = int(input())
        self.water += x
        print("Write how many ml of milk do you want to add:")
        x = int(input())
        self.milk += x
        print("Write how many grams of coffee beans do you want to add:")
        x = int(input())
        self.beans += x
        print("Write how many disposable cups of coffee do you want to add:")
        x = int(input())
        self.cups += x
        pass

    def take(self):
        print("I gave you", self.money)
        self.money = 0
        pass


machine = CoffeMachine(400, 540, 120, 9, 550)

while True:
    print("Write action (buy, fill, take, remaining, exit)")
    action = input()
    if action == "buy":
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        option = input()
        machine.buy(option)
        # state()
    elif action == "fill":
        machine.fill()
        # state()
    elif action == "take":
        machine.take()
        # state()
    elif action == "remaining":
        machine.state()
    elif action == "exit":
        break
