class PiggyBank:
   def __init__(self, dollars, cents):
       self.dollars = dollars
       self.cents = cents


   def add_money(self, d, c):
       self.deposit_dollars = d
       self.deposit_cents = c
       self.dollars += d
       self.cents += c
       while self.cents >= 100:
           self.cents -= 100
           self.dollars += 1
       pass



