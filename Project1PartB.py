print('Part One - Project B: Prime Choice\n')

min = int(input('Prime Numbers starting with: '))
max = int(input('and ending with: '))

if min > max: 
    print('\nIncorrect input: {} is greater than {}'.format(min,max) + '\nThe numbers have been automatically switched.\n')
    temp = min
    min = max 
    max = temp

print('Prime Numbers in the range from: {} and {} are:'.format(min,max))

for i in range(min,max):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        print(str(i) , 'is prime')

print('\nEnd Part One - Project B\nShon Haskaj shaskaj 251372286')
