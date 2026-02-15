def factorial(a):
    if a == 0 or a == 1:
        return 1
    else:
        return a * factorial(a-1)

n=int(input('enter the number:'))
if n<0:
    raise ValueError('Integer must be positive')
else:
    ans=factorial(n)
    print(f'the factorial of {n} is {ans}')