# a function that will find a number is a prime
known_primes = [2,3]
def is_prime(n):
    # print n
    total_known_primes = len(known_primes)
    for i in range(0, total_known_primes):
        if(n % known_primes[i] == 0):
            # this is divisable by a prime number.
            # it cannot be prime
            return False
        else:
                # its not divisible by this one... but that doesnt mean 
                # its not prime. its just not divisable by this number
            continue
    # we went through all known primes, and never hit our redturn false...
    # which means, this wasnt divisable by any known prime,
    # so it must be a prime append
    known_primes.append(n)
    if(i == total_known_primes):
        return True

print is_prime(6)
print is_prime(8)