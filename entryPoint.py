import nash
import util

ClientInput = util.Util.fromFileToMap(util.Util.parse().filePath)

GovernmentPayoffs = ['Government',
                     ('L', 'L', 0),
                     ('L', 'H', -1),
                     ('H', 'L', 0.5),
                     ('H', 'H', -0.5)]
PublicPayoffs = ['Public',
                 ('L', 'L', 0),
                 ('L', 'H', -1),
                 ('H', 'L', -1),
                 ('H', 'H', 0)]

nash.calculate_nash(GovernmentPayoffs, PublicPayoffs)

for i in range(0, int(util.Util.parse().iterations)):
    nash.time_scales_game(ClientInput, GovernmentPayoffs, PublicPayoffs)

print(" ")
