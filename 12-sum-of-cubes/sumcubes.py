n = int(input('Input : '))
sumofcubes = sum([x*x*x for x in [*range(1, n+1)]])
print('Output: ', sumofcubes)
