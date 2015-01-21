primes = [2]
candidate = 3
while candidate < 100:
    for prime in primes:
        if candidate % prime== 0:
            print ("%d divides %d") (prime,candidate)
            break
    else:
        print ("%d is prime" % (candidate))
        primes.appened(candidate)
        
    candidate += 2
