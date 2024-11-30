# Curtis Van Ausdal
# CS 3320
# Module 4 - Sine Function
'''Write a function, mysine(x), that computes the value sine function with x as its
argument.
Your program will do the followings:
▪ Reduce the input x to be in [− π/2, π/2],
▪ Use a Taylor’s Series up to 21 x 21! term (you can hard code this in your function or you can write a
findn routine to determine the number of terms that are required),
▪ Handle small angles, i.e., return as sin ( ) when 2 ≤ , x x x ε
▪ Handle large angles, i.e., return nan when > 109 x
Submit your source and the output for the angles listed below.'''
import math
import sys

base = sys.float_info.radix
eps = sys.float_info.epsilon
prec = sys.float_info.mant_dig
inf = math.inf

def fact(x):
    '''finds value of factorial x '''
    if x == 0 or 0.0 or 0.00:  # if x is zero return 1, this is 0 factorial special condition
        return 1
    fact_list = []
    for i in range(x + 1):  # range is x +1, we append values to list and multiply all things in list
        fact_list.append(x)
        x = x - 1
    fact_list = fact_list[:-1]
    result = 1
    for num in fact_list:
        result = result * num
    return result

def mysine(x):
    """return sin(x) function result using taylor series with 21 terms """
    if x**2 <= eps and x != 0:  # first check small angle
        return x
    if x > 1e9 or x < -1e9:  # large angle is outside of -1x10^9 or 1x10^9
        return math.nan
    if x <= (math.pi / 2) and x >= (-(math.pi / 2)):
        condition = True  # x is between correct parameters
    else:
        condition = False  # x is not between -pi/2 and pi/2
    if condition is False:
        N = round(x / math.pi)
        t = x - N * math.pi
        x = t
    if condition is True:  # if parameters are correct just pass, don't adjust x value
        pass
    n = 21  # number of terms required, instructions say I am allowed to hard code this portion
    termResultList = []  # initialize a term list, this is so I can print it and check terms individually if needed
    for i in range(1, n + 2):  # make terms
        term = i
        if i % 2 != 0:  # every odd term in this Taylor's series is 0 because sin(0) is 0
            term_result = 0
            termResultList.append(term_result)
        elif i % 2 == 0:  # checks even term
            if i % 4 == 0:  # every other even term will have a negative sign in front of value
                factorial = fact(term - 1)
                exponent = term - 1
                term_result = -((x ** exponent) / (factorial))  # x^e / factorial(term)
                termResultList.append(term_result)
            else:  # if not i%4, the value of this term will be positive
                factorial = fact(term - 1)
                exponent = term - 1
                term_result = ((x ** exponent) / (factorial))
                termResultList.append(term_result)
    result = sum(termResultList)  # add all terms together (summation) to get final result
    return result

print('\n')
print(mysine(1.0e-08))
print(mysine(0.00001))
print(mysine(0))
print(mysine(math.pi / 2))
print(mysine(math.pi))
print(mysine(100))
print(mysine(-1000))
print(mysine(999999999))
print(mysine(-1000000001))
