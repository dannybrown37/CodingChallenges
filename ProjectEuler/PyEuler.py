def main():
    problem_8()


def problem_8():
    """
    Largest product in a series
    Problem 8
    The four adjacent digits in the 1000-digit number that have the greatest
    product are 9 x 9 x 8 x 9 = 5832.

    Find the thirteen adjacent digits in the 1000-digit number that have the
    greatest product. What is the value of this product?
    """
    num = (
        '73167176531330624919225119674426574742355349194934'
        '96983520312774506326239578318016984801869478851843'
        '85861560789112949495459501737958331952853208805511'
        '12540698747158523863050715693290963295227443043557'
        '66896648950445244523161731856403098711121722383113'
        '62229893423380308135336276614282806444486645238749'
        '30358907296290491560440772390713810515859307960866'
        '70172427121883998797908792274921901699720888093776'
        '65727333001053367881220235421809751254540594752243'
        '52584907711670556013604839586446706324415722155397'
        '53697817977846174064955149290862569321978468622482'
        '83972241375657056057490261407972968652414535100474'
        '82166370484403199890008895243450658541227588666881'
        '16427171479924442928230863465674813919123162824586'
        '17866458359124566529476545682848912883142607690042'
        '24219022671055626321111109370544217506941658960408'
        '07198403850962455444362981230987879927244284909188'
        '84580156166097919133875499200524063689912560717606'
        '05886116467109405077541002256983155200055935729725'
        '71636269561882670428252483600823257530420752963450'
    )

    largest = 0
    for x in range(0, 987):
        pie = num[x:x+13]
        result = 1
        for digit in pie:
            result = result * int(digit)
        if result > largest:
            largest = result

    print largest




def problem_7():
    """
    10001st prime
    Problem 7
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
    we can see that the 6th prime is 13.

    What is the 10,001st prime number?
    """
    def check_prime(num):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    return False
            else:
                return True
        else:
            return False

    count = 0
    for x in range(2, 1000000):
        prime = check_prime(x)
        if prime:
            count += 1
            if count == 10001:
                print x
                break



def problem_6():
    """
    Sum square difference
    Problem 6
    The sum of the squares of the first ten natural numbers is,

    12 + 22 + ... + 102 = 385
    The square of the sum of the first ten natural numbers is,

    (1 + 2 + ... + 10)2 = 552 = 3025
    Hence the difference between the sum of the squares of the first ten
    natural numbers and the square of the sum is 3025 - 385 = 2640.

    Find the difference between the sum of the squares of the first one
    hundred natural numbers and the square of the sum.
    """
    sum_of_squares = 0
    square_of_sums = 0
    for x in range(1, 101):
        sum_of_squares += x**2
        square_of_sums += x
    square_of_sums = square_of_sums**2
    answer = square_of_sums - sum_of_squares
    print "Answer is %s" % answer


def problem_5():
    """
    Smallest multiple
    Problem 5
    2520 is the smallest number that can be divided by each of the numbers
    from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of
    the numbers from 1 to 20?
    """
    answer = False
    for x in range(2000000, 1000000000, 20):
        if answer:
            break
        count = 0
        for y in range(1, 21):
            if x % y == 0:
                count += 1
                if count is 20:
                    answer = x
            else:
                break
    print "The answer is " + str(answer)


def problem_4():
    """
    Largest palindrome product
    Problem 4
    A palindromic number reads the same both ways. The largest palindrome made
    from the product of two 2-digit numbers is 9009 = 91 x 99.

    Find the largest palindrome made from the product of two 3-digit numbers.
    """
    def is_palindrome(num):
        num = str(num)
        rev = num[::-1]
        if num == rev:
            return True
        else:
            return False

    largest = 0
    for x in range(100, 1000):
        for y in range(100, 1000):
            num = x * y
            if is_palindrome(num) and num > largest:
                largest = num
            else:
                pass

    print largest


def problem_3():
    from itertools import islice, count
    from math import sqrt
    """
    Problem 3
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?
    """
    big = 600851475143
    littles = []
    for x in range(1, big/10000): # arbitrarily divided until I found one that
        if big % x == 0:          # worked without a memory error
            littles.append(x)

    def is_prime(n):
        return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

    primes = []
    for item in littles:
        if is_prime(item):
            primes.append(item)

    print primes


def problem_2():
    """
    Problem 2
    Each new term in the Fibonacci sequence is generated by adding the previous
    two terms. By starting with 1 and 2, the first 10 terms will be:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

    By considering the terms in the Fibonacci sequence whose values do not
    exceed four million, find the sum of the even-valued terms.
    """
    total = 0
    fibonacci = [1, 1] # just to get us started

    while fibonacci[len(fibonacci)-1] < 4000000:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
        if fibonacci[len(fibonacci)-1] % 2 == 0:
            total += fibonacci[len(fibonacci)-1]
    print total


def problem_1():
    """
    Problem 1
    If we list all the natural numbers below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
    """
    total = 0
    for x in range(0, 1000):
        if x % 3 == 0 or x % 5 == 0:
            total += x

    print total


if __name__ == '__main__':
    main()
