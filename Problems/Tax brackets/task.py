income = int(input())

if income <= 15527:
    tax = 0
elif income <= 42707:
    tax = 15
elif income <= 132406:
    tax = 25
else:
    tax = 28

payment = round(income*(tax/100))

print(f'The tax for {income} is {tax}%. That is {payment} dollars!')