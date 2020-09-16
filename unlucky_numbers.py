for num in range(1, 21):
    if num == 4 or num == 13:
        state = 'UNLUCKY ONE'
    elif num % 2 != 0:
        state = 'Number is odd'
    else:
        state = 'Number is even'
    print(f'{num} Number is {state}')