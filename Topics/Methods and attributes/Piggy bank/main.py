class PiggyBank:
    # create __init__ and add_money methods
    def __init__(self, d, c):
        self.dollars = d
        self.cents = c

    def add_money(self, deposit_dollars, deposit_cents):
        self.dollars += deposit_dollars
        self.dollars += (deposit_cents + self.cents) // 100
        self.cents += (deposit_cents + self.cents) % 100 - 1


#bank = PiggyBank(1, 1)

#bank.add_money(0, 88)
#print(bank.dollars, bank.cents)