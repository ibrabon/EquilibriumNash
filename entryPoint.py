import globalConstants
import nash
import util

clientInput = util.Util.fromFileToMap(util.Util.parse().filePath)

governmentPeriod = clientInput.get(globalConstants.governmentTimePeriod)
governmentStrategy = clientInput.get(globalConstants.governmentScalarStrategy)
publicPeriod = clientInput.get(globalConstants.publicTimePeriod)
publicStrategy = clientInput.get(globalConstants.publicScalarStrategy)

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

nash.method_name(GovernmentPayoffs, PublicPayoffs)

print(" ")
