import copy
import random
import time
from pprint import pprint

COUNTER = 0
START_TIME = time.time()


# This function generates fibonacci row till mentioned value
# e.g. for number 11: [0, 1, 1, 2, 3, 5, 8, 13]
# e.g. for number 13: [0, 1, 1, 2, 3, 5, 8, 13]
def generate_fibonacci(value):
    if value == 0:
        return [0]
    else:
        a, b = 0, 1
        result = [a, b]
        while b < value:
            c = a
            a = b
            b = c + b
            result.append(b)
        return result


# This method count value based on combination vector ([0, 1, 0, 0])
def count_value(fibonacci, combination):
    sum = 0
    for i in range(0, len(combination)):
        if combination[i] > 0:
            sum = sum + fibonacci[i]
    return sum


def check_forward(fibonacci, combination, number, position):
    if position == len(combination) - 1:
        return True
    actual_value = count_value(fibonacci, combination)
    if actual_value > number:
        return False
    else:
        return True


def forwardchecking_algorithm(fibonacci, combination, number, index, accumulator):
    global COUNTER
    COUNTER = COUNTER + 1
    actual_value = count_value(fibonacci, combination)
    if actual_value == number:
        if combination not in accumulator:
            accumulator.append(combination.copy())
            print("iteration number: " + str(COUNTER))
            print("solutions number: " + str(len(accumulator)))
            print("Execution time: " + str(time.time() - START_TIME))
            print("----------------")
    elif actual_value > number:
        return accumulator
    else:
        for d in range(index, len(combination)):
            if combination[d] == 0:
                combination1 = combination.copy()
                combination1[d] = 1
                is_forward = check_forward(fibonacci, combination1, number, d)
                if is_forward:
                    forwardchecking_algorithm(fibonacci, combination1, number, d, accumulator)
    return accumulator


def backtracking_algorithm(fibonacci, combination, number, index, accumulator):
    global COUNTER
    COUNTER = COUNTER + 1
    #print(COUNTER)
    #print(combination)
    actual_value = count_value(fibonacci, combination)
    if actual_value == number:
        if combination not in accumulator:
            accumulator.append(combination.copy())
            print("iteration number: " + str(COUNTER))
            print("solutions number: " + str(len(accumulator)))
            print("Execution time: " + str(time.time() - START_TIME))
            print("----------------")
    elif actual_value > number:
        return accumulator
    else:
        for d in range(index, len(combination)):
            if combination[d] == 0:
                combination1 = combination.copy()
                combination1[d] = 1
                backtracking_algorithm(fibonacci, combination1, number, d, accumulator)
    return accumulator


def print_result(fibonacci, result):
    result = result.copy()
    for row in result:
        for i in range(0, len(row)):
            if row[i] == 1:
                row[i] = fibonacci[i]
            else:
                row[i] = "."
    pprint(result)


def find_solutions(value):
    fibonacci = generate_fibonacci(value)[2:-1]
    random.shuffle(fibonacci)
    print("Fibonacci row", fibonacci)
    if method == 'b':
        result = backtracking_algorithm(fibonacci, [0] * len(fibonacci), value, 0, [])
    if method == 'f':
        result = forwardchecking_algorithm(fibonacci, [0] * len(fibonacci), value, 0, [])
    print("iteration number: " + str(COUNTER))
    print("Solutions number: " + str(len(result)))
    print_result(fibonacci, copy.deepcopy(result))


# enter to the program
if __name__ == '__main__':
    value = 64  # number to be divided
    method = 'f'  # 'b' - backtraking, 'f' - forwardchecking
    find_solutions(value)
    print("Execition time: " + str(time.time() - START_TIME))
