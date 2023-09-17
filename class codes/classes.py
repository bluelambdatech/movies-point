from function import factorial


name = "Omolewa"


class Vehicle:
    pass

# dunder methods


# method - factorial, permutation, combination

class Calculus:

    def __init__(self, n, r):

        self.n = n
        self.r = r
        assert self.n >= self.r, f"Not Possible: {self.n} must be greater than {self.r}"

    def permutation(self):
        return factorial(self.n) / factorial(self.n - self.r)

    def combination(self):

        return factorial(self.n) / (factorial(self.n - self.r) * factorial(self.r))
    # write the combination


calc = Calculus(20, 4)

print(calc.permutation())

print(calc.combination())


