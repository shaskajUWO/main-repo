def fib(n):
    if n <= 2 and n < 0:
        return 1
    elif (n == 0):
        return 0
    else:
         return fib(n - 2) + fib(n - 1)

print('Project One <01> - Part A : Fibonacci Sequence')

rang = int(input('Sequence ends at:'))

for i in range(rang+1):
    print(str(i) + ': ' + str(fib(i)) , f'{fib(i):,}')

print('\nEND: Project One <01> - Part A\nShon Haskaj shaskaj 251372286')