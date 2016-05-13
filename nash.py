import math
import random

import globalConstants
import util


class Player:
    def __init__(self, name, order, strategy_space, payoffs, choice, suboptimal, strategies, state, game_play):
        self.name = name
        self.order = order
        self.strategy_space = strategy_space
        self.payoffs = payoffs
        self.choice = choice
        self.suboptimal = suboptimal
        self.strategies = strategies
        self.state = state
        self.game_play = game_play

    def process_game(self, G):
        for i in range(0, len(G)):
            X = G[i]
            if X[0] == self.name:
                for j in range(1, len(X)):
                    Branch = X[j]
                    Alternative = list(Branch)
                    del Alternative[len(Alternative) - 1]
                    self.strategy_space = self.strategy_space + [tuple(Alternative)]
                    self.payoffs = self.payoffs + [Branch[len(Branch) - 1]]

    def evaluate(self):
        X = []
        for i in range(0, len(self.strategy_space)):
            Alternative1 = self.strategy_space[i]
            for j in range(0, len(self.strategy_space)):
                Alternative2 = self.strategy_space[j]
                if Alternative1 != Alternative2:
                    if len(Alternative1) == len(Alternative2):
                        Compare = 0
                        for k in range(0, len(Alternative1) - 1):
                            if Alternative1[k] == Alternative2[k]:
                                Compare = Compare + 0
                            else:
                                Compare = Compare + 1
                        if Compare == 0:
                            PayoffCompare = [self.payoffs[i], self.payoffs[j]]
                            M = max(PayoffCompare)
                            if self.payoffs[i] == M:
                                self.choice = Alternative1
                                X = X + [self.choice]
                            else:
                                self.suboptimal = self.suboptimal + [Alternative1]
                            if self.payoffs[j] == M:
                                self.choice = Alternative2
                                X = X + [self.choice]
                            else:
                                self.suboptimal = self.suboptimal + [Alternative2]

        X = set(X)
        self.suboptimal = set(self.suboptimal)
        self.strategies = list(X - self.suboptimal)
        print("\nStrategies selected by " + self.name + ":")
        print(self.strategies)
        for l in range(0, len(self.strategies)):
            strategy = self.strategies[l]
            for m in range(0, len(strategy)):
                O = self.order[m]
                self.state[O] = strategy[m]
            self.game_play = self.game_play + [tuple(self.state)]


class Game:
    def __init__(self, players, structure, optimal):
        self.players = players
        self.structure = structure
        self.optimal = optimal

    def nash(self, GP):
        Y = set(GP[0])
        for i in range(0, len(GP)):
            X = set(GP[i])
            Y = Y & X
        self.optimal = list(Y)
        if len(self.optimal) != 0:
            print("\nThe pure strategies Nash equilibrium  are:")
            for k in range(0, len(self.optimal)):
                print(self.optimal[k])
        else:
            print("\nThis game has no pure strategies Nash equilibrium!")


class TimeScaleGame(Game):
    def __init__(self, players, structure, optimal, government_period, public_period, government_strategy,
                 public_strategy):
        super().__init__(players, structure, optimal)
        self.government_period = government_period
        self.public_period = public_period
        self.government_strategy = government_strategy
        self.public_strategy = public_strategy

    def play(self):
        fullTime = util.lcm(self.government_period, self.public_period)
        self.government_strategy = self.getStrategyForAllPeriod(self.government_strategy, self.government_period,
                                                                fullTime)
        self.public_strategy = self.getStrategyForAllPeriod(self.public_strategy, self.public_period, fullTime)
        self.payoff = [0, 0]
        for x in range(0, fullTime):
            self.payoff = util.add(self.getPayoff(x), self.payoff)
        return self.payoff

    def getPayoff(self, x):
        g_strat = self.government_strategy[x]
        p_strat = self.public_strategy[x]
        summ = []
        for i in range(0, len(self.structure)):
            X = self.structure[i]
            for d in range(0, len(self.players)):
                if X[0] == self.players[d]:
                    for j in range(1, len(X)):
                        Branch = X[j]
                        Alternative = list(Branch)
                        del Alternative[len(Alternative) - 1]
                        if Alternative == [g_strat, p_strat]:
                            summ.append(list(Branch)[len(Branch) - 1])
        return summ


    def getStrategyForAllPeriod(self, strategy, period, fullTime):
        new_strategy = []
        changePeriod = fullTime / period
        tmp = -1
        for x in range(0, fullTime):
            index = math.floor(x / changePeriod)
            if index != tmp:
                probability = float(strategy[index])
                rand = random.randrange(0, 100) / 100
                if probability > rand:
                    new_strategy.append('H')
                else:
                    new_strategy.append('L')
                tmp = index
            else:
                new_strategy.append(new_strategy[x - 1])
        return new_strategy


def calculate_nash(government_payoffs, public_payoffs):
    # game(players,structure,plays,optimal)
    game = Game(('Government', 'Public'), [government_payoffs, public_payoffs], None)
    # player(name,order,strategySpace,payoffs,choice,suboptimal,strategies,state,gameplay):
    player1 = Player('Government', (1, 0), [], [], None, [], None, [0, 0], [])
    player2 = Player('Public', (0, 1), [], [], None, [], None, [0, 0], [])
    players = [player1, player2]
    for i in range(0, len(players)):
        players[i].process_game(game.structure)
        players[i].evaluate()
    GP = []
    for i in range(0, len(players)):
        X = players[i].game_play
        GP = GP + [X]
    game.nash(GP)


def time_scales_game(request, government_payoffs,
                     public_payoffs):
    government_period = request.get(globalConstants.GOVERNMENT_TIME_PERIOD)
    public_period = request.get(globalConstants.PUBLIC_TIME_PERIOD)
    government_strategy = str(request.get(globalConstants.GOVERNMENT_SCALAR_STRATEGY)).split(',')
    public_strategy = str(request.get(globalConstants.PUBLIC_SCALAR_STRATEGY)).split(',')

    game = TimeScaleGame(('Government', 'Public'), [government_payoffs, public_payoffs], None, int(government_period),
                         int(public_period), government_strategy, public_strategy)
    return game.play()

