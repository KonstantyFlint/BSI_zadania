import utils
import math

def z_1_a(reliability_m, time_m, time_r):
    '''
    Deduces probability of survival at point in time.
    
    Parameters:
    reliability_m (float): measured reliability
    time_m (float): time of measurement
    time_r (float): request time

    Returns:
    float: probability of survival up to time_r
    '''
    rel_f = utils.deduce_reliability_function(time_m, reliability_m)
    return rel_f(time_r)

def z_1_b(reliability_m, time_m, time_survived, time_r):
    '''
    Deduces probability of survival at point in time. Takes already survived time into account.

    Parameters:
    reliability_m (float): measured reliability
    time_m (float): time of measurement
    time_survived (float): point up to which the machine has survived
    time_r (float): request time

    Returns:
    float: probability of survival up to time_r
    '''
    rel_f = utils.deduce_reliability_function(time_m, reliability_m)
    if time_r < time_survived:
        return 1
    else:
        return rel_f(time_r) / rel_f(time_survived)

def z_2(failure_rate_a, failure_rate_b, count, time):
    '''
    Estimates number of components to be replaced.

    Parameters:
    failure_rate_a (float): failure rate of component A
    failure_rate_b (float): failure rate of component B
    count (int): count of each component (counts are assumed to be equal)
    time (float): useful life

    Returns:
    {float, float}: estimated number of each component to be replaced in useful life
    '''
    return {failure_rate_a * count * time, failure_rate_b * count * time}

def z_3(failure_rate, time_survived, time_r):
    '''
    Calculates reliability at certain time, given failure rate.
    
    Parameters:
    filure_rate (float): failure rate of an item
    time_survived (float): time the item has survived
    time_r (float): request time

    Returns:
    float: probability of survival up to request time
    '''
    
    rel_f = utils.make_reliability_function(failure_rate)
    if time_survived > time_r:
        return 1
    else:
        return rel_f(time_r) / rel_f(time_survived)

def z_4(reliability, time):
    '''
    Calculates desired failure rate and MTBF
    
    Parameters:
    reliability (float): minimal desired reliability
    time (float): useful life
    
    Returns:
    failure_rate (float): maximum permissible failure rate
    MTBF (float): minimum permissible mean time between failures
    '''
    failure_rate = (1 - reliability)/time
    MTBF = 1 / failure_rate
    return {"failure rate":failure_rate, "MTBF": MTBF}

def z_5(failure_rate, warranty_fail):
    '''
    Calculates optimal warranty

    Parameters:
    failure_rate (float) - failure rate of the machine
    warranty_fail (float) - maximal permissible fraction of machines to fail during warranty (range 0.0 to 1.0)

    Returns:
    float: optimal warranty
    '''
    return  - (math.log(1 - warranty_fail) / failure_rate)
