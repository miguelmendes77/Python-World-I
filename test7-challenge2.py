n1 = float(input('Enter the first note: '))
n2 = float(input('Enter the second note: '))

n = (n1 + n2) / 2

print('\nThe overall average is 7.0!')

print('\nIts average is ({:.1f}).' .format(n))

print('\nYou are above average.' if n > 7 else '\nYou are below average.')

print('\n-----END-----')