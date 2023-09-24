

class Activities:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.balance = 0

    def shout(self):
        self.fullName = f"{self.fname} {self.lname}"

        return self.fullName

    def say(self):
        print(self.fname)

    def update(self):
        self.fname = self.fname.upper()

    def credit(self, amt):
        self.balance += amt


"""Create a class called SavingsAccount that represents an actual savings account in a bank.
# It has two properties: funds and rate_of_interest.
# The class should also have a method called debit() that decreases the funds by the specified amount and
# a method called credit() that adds to the existing balance.
# Also, define a third method to transfer the interest amount to the savings account.

"""

def debit():
    pass


class SavingsAccount:
    def __init__(self, funds, rate_of_interest):
        """

        :param funds:
        :param rate_of_interest: float -> 2% means 0.02
        """
        self.funds = funds
        self.rate_of_interest = rate_of_interest / 100

    def debit(self, amt):
        # self.funds = self.funds - amt
        self.funds -= amt
        # self.decreases = self.decreases - funds

    def debit(self):
        print("Omolewa")

    def credit(self, amt):
        self.funds += amt

    def transfer_interest(self):
        self.funds = self.funds + self.funds * self.rate_of_interest
        #self.funds *= self.funds * self.rate_of_interest
        # pass  # Don't know what to do here

    def get_funds(self):
        return self.funds

    def run(self):
        self.debit(200)
        self.credit(100000)
        self.transfer_interest()
        balance = self.get_funds()

        return balance


class Bank(SavingsAccount):
    def __init__(self):
        super(SavingsAccount, self).__init__(200, 2)

        self.bankName = "Oceanic Bank"

    def shoutshout(self):
        pass


bank = Bank()

acct = SavingsAccount(1000, 2)

print(acct.run())



