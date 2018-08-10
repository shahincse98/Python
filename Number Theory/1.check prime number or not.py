num = int(input('Enter a number: '))
c = 0
if num > 1:
    for number in range(2, num):
        if num % number == 0:
            c += 1

    if c == 0:
        print('YES!', num, 'is prime')
    else:
        print('SORRY!', num, 'is not prime')

else:
    print('SORRY!', num, 'is not prime')
    
