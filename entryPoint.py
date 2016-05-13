from datetime import datetime
import nash
import util

ClientInput = util.fromFileToMap(util.parse().filePath)

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


time = datetime.timestamp(datetime.now())
stop = int(util.parse().iterations)
mat = [[0] * stop for i in range(2)]
for i in range(0, stop):
    game = nash.time_scales_game(ClientInput, GovernmentPayoffs, PublicPayoffs)
    for j in range(0, 2):
        mat[j][i] = game[j]

util.create_all_stats(mat[0], 'Government', time)
util.create_all_stats(mat[1], 'Public', time)

print(" ")
