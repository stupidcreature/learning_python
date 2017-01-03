import math


def initialize_bool_array(array_size, initial_value=False):
    # there must be a way to do that more efficiently
    array_of_primes = []
    for i in range(0, array_size + 1):
        array_of_primes.append(initial_value)
    return array_of_primes


def generate_prime_naive(max_prime, print_all_numbers=True):
    print("calculate prime numbers up to {} using the naive method".format(max_prime))

    # first create and initialize the result array
    array_of_primes = initialize_bool_array(max_prime)

    for i in range(2, max_prime):

        # start with the assumption that i is prime and try to disprove it
        is_prime = True

        for j in range(2, i - 1):
            if i % j == 0:
                is_prime = False
                break

        if is_prime:
            array_of_primes[i] = True
            if print_all_numbers:
                print('{} is a prime number'.format(i))

    return array_of_primes


def generate_prime_eratosthenes(max_prime, print_all_numbers=True):
    print("calculate prime numbers up to {} using the sieve of Eratosthenes".format(max_prime))

    # first create and initialize the result array
    array_of_primes = initialize_bool_array(max_prime, True)

    # round before converting to int, otherwise the value will be truncated and
    # might be too small (e.g. int(sqrt(1000)) == int(31.6) == 31 and not 32, as required
    for i in range(2, int(round(math.sqrt(max_prime)))):
        if array_of_primes[i]:
            for j in range(i * i, max_prime + 1, i):
                array_of_primes[j] = False

    # 0 and 1 are not considered prime numbers
    array_of_primes[0] = False
    array_of_primes[1] = False
    if print_all_numbers:
        for i in range(2, max_prime):
            if array_of_primes[i]:
                print('{} is a prime number'.format(i))

    return array_of_primes


def primes():
    # 2 functions to generate prime numbers
    max_prime = 1000
    primes_naive = generate_prime_naive(max_prime, False)
    primes_eratosthenes = generate_prime_eratosthenes(max_prime, False)

    prime_count_naive = primes_naive.count(True)
    prime_count_eratosthenes = primes_eratosthenes.count(True)
    print("Up until {} we have found {} prime numbers with the naive method and {} prime numbers "
          "using the sieve of Eratosthenes.".format(max_prime, prime_count_naive, prime_count_eratosthenes))