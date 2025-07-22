def isprime(number):
    isprime = True
    if number == 2:
        isprime = True
    elif number % 2 == 0 or number == 1:
        isprime = False
    else:
        for i in range(3, number//2):
            if number % i == 0:
                isprime = False
                return isprime
    return isprime
            

