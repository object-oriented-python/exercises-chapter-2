import numpy as np

def isprime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(np.sqrt(num)) + 1):
            if num % i == 0:
                return False
        
        return True