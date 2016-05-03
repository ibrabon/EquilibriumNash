class Equilibrium:

    def makeStep(self, amount):

        for x in range(0, int(0 if amount is None else amount)):
            print("Step " + str(x))

