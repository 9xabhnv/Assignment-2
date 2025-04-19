# Task 1

n = int(input('Enter a number: '))
if n % 2 == 0:
    print(n, 'is an even number.')
else:
    print(n, 'is an odd number.')

# ------------------------------------------------------------------------------------------------

# Task 2

sum = 0
for i in range(1, 51):
    sum = sum + i
print('The sum of number from 1 to 50 is:', sum)
