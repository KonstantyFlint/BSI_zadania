import math

def make_reliability_function(failure_rate):
    '''
    input: failure rate
    output: exponential reliability function
    '''
    return lambda t : math.exp(-1 * failure_rate * t)

def deduce_reliability_function(time, reliability):
    '''
    input: reliability at a point in time
    output: exponential reliability function
    '''
    failure_rate = math.log(reliability) / time / -1
    return make_reliability_function(failure_rate)
