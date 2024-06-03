import time
import random

def random_list(size, low, high):
    """
    return a list of length size populated with random ints in the range low-->high
    Parameters:
            size: length of desired list
            low: smallest value present in the list
            high: largest value present in the list

        Returns:
            a list of length size populated with random ints in the range low-->high
    """
    random.seed()
    a = [random.randint(low, high) for r in range(size)]
    return a

def time_this(function, *args):
    """time_this measures the elapsed time when a function is executed

        Parameters:
            function: Reference to function whose execution time is being measured
            *args: comma-separated list of arguments to function

        Returns:
            a tuple representing the elapsed time and the result returned by the function

    """

    start = time.perf_counter()  # record initial time
    result = function(*args)  # call the specified function, passing it the specified parameters
    end = time.perf_counter()  # record final time
    return float("%.20f" % (end - start))

    # result            This is from the original time_this function. I have removed this code for the word_ladder assignment
    # return elapsed time and value returned by function
