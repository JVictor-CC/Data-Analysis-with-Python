# This entrypoint file to be used in development. Start by reading README.md
import mean_var_std
from unittest import main

results = mean_var_std.calculate([0,1,2,3,4,5,6,7,8])

print('\nmean:',results['mean'])
print('\nvariance:',results['variance'])
print('\nstandard deviation:',results['standard deviation'])
print('\nmax:',results['max'])
print('\nmin:',results['min'])
print('\nsum:',results['sum'])

# Run unit tests automatically
main(module='test_module', exit=False)