print('Project One <01> - Part C: The Moore the Merrier')

num_of_transistors = int(input("Starting Number of transistors: "))
year = int(input('Starting year: '))
total_years = int(input('Total Number of Years: '))

print('\nYEAR : TRANSISTORS : FLOPS:')

for i in range(0, total_years+2, 2):
    if num_of_transistors*50 >= 10**24:
        print('%d %s %.2f yottaFLOPS %s' % (year, f'{num_of_transistors:,}', num_of_transistors*50/10**24, f'{num_of_transistors*50:,}'))
    elif num_of_transistors*50 >= 10**21:
        print('%d %s %.2f zetaFLOPS %s' % (year, f'{num_of_transistors:,}', num_of_transistors*50/10**21, f'{num_of_transistors*50:,}'))
    elif num_of_transistors*50 >= 10**18:
        print('%d %s %.2f exaFLOPS %s' % (year, f'{num_of_transistors:,}', num_of_transistors*50/10**18, f'{num_of_transistors*50:,}'))
    elif num_of_transistors*50 >= 10**15:
        print('%d %s %.2f petaFLOPS %s' % (year, f'{num_of_transistors:,}', num_of_transistors*50/10**15, f'{num_of_transistors*50:,}'))
    elif num_of_transistors*50 >= 10**12:
        print('%d %s %.2f teraFLOPS %s' % (year, f'{num_of_transistors:,}', num_of_transistors*50/10**12, f'{num_of_transistors*50:,}'))
    elif num_of_transistors*50 >= 10**9:
        print('%d %s %.2f gigaFLOPS %s' % (year, f'{num_of_transistors:,}', num_of_transistors*50/10**9, f'{num_of_transistors*50:,}'))
    elif num_of_transistors*50 >= 10**6:
        print('%d %s %.2f megaFLOPS %s' % (year, f'{num_of_transistors:,}', num_of_transistors*50/10**6, f'{num_of_transistors*50:,}'))
    elif num_of_transistors*50 >= 10**3:
        print('%d %s %.2f kiloFLOPS %s' % (year, f'{num_of_transistors:,}', num_of_transistors*50/10**3, f'{num_of_transistors*50:,}'))
    
    year += 2
    num_of_transistors *= 2

print('\nEND: Prohject One <01> - Part C\nShon Haskaj shaskaj 251372286')