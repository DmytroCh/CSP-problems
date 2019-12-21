import copy
import random
from pprint import pprint
import time


COUNTER = 0
START_TIME = time.time()


def create_variables(size):
    variables = list()
    domain = list(range(0, size))
    for i in range(0, size):
        random.shuffle(domain)
        variables.append([None, domain])
    return variables


# This method checking if any variable has empty domain, if yes - returns true
def are_empty_domains(variables):
    for i in range(0, len(variables)):
        if len(variables[i][1]) == 0:
            return True
    return False


# This method check if all variables has assigned values
def are_values_assigned(variables):
    for i in range(0, len(variables)):
        if variables[i][0] is None:
            return False
    return True


# This method removes given value from domains of all variables
def remove_taken_values(value, variables):
    return list(map(lambda var: [var[0], list(filter(lambda x: not x == value, var[1]))], variables))


def check_diagonals(values):
    if len(values) < 2:
        return True
    else:
        pointer = len(values) - 2
        actual_position_x = len(values) - 1
        while pointer >= 0:
            diff_x = abs(actual_position_x - pointer)
            diff_y = abs(values[actual_position_x] - values[pointer])
            pointer = pointer - 1
            if diff_x == diff_y:
                return False
        return True


# This method check constraints
def check_constraints(variables, position):
    support = list(map(lambda variable: variable[0], variables))
    support = list(filter(lambda value: value is not None, support))
    # duplicates checking, it means queens stay in one row
    if len(support) != len(set(support)):
        return False
    else:
        return check_diagonals(support[:position + 1])


# This method solves CSP problem by backtracking algorithm
def backtracking_algorithm(variables, index, accumulator):
    global COUNTER
    if are_values_assigned(variables):
        accumulator.append(variables)
        print("iteration number: " + str(COUNTER))
        print("solutions number: " + str(len(accumulator)))
        print("Execution time: " + str(time.time() - START_TIME))
        print("----------------")
    elif are_empty_domains(variables):
        return accumulator
    else:
        length = len(variables[index][1])
        for d in range(0, length): # [wartość, [dziedzina]]
            variables[index][0] = variables[index][1][d]
            COUNTER = COUNTER + 1
            #print(variables)
            variables1 = copy.deepcopy(variables)
            #variables1 = remove_taken_values(variables[index][1][d], variables1)
            if check_constraints(variables, index):
                backtracking_algorithm(variables1, index + 1, accumulator)

    return accumulator


def is_forward_way(variables, index):
    new_domain = []
    for i in range(0, len(variables[index][1])):
        next_value = variables[index][1][i]
        variables[index][0] = next_value
        if check_constraints(variables, index):
            new_domain.append(next_value)
    return new_domain


# This method solves CSP problem by backtracking algorithm
def forwardchecking_algorithm(variables, index, accumulator):
    global COUNTER
    if are_values_assigned(variables):
        accumulator.append(variables)
        print("iteration number: " + str(COUNTER))
        print("solutions number: " + str(len(accumulator)))
        print("Execution time: " + str(time.time() - START_TIME))
        print("----------------")
    elif are_empty_domains(variables):
        return accumulator
    else:
        length = len(variables[index][1])
        for d in range(0, length):
            variables[index][0] = variables[index][1][d]
            COUNTER = COUNTER + 1
            #print(variables)
            variables1 = copy.deepcopy(variables)
            #variables1 = remove_taken_values(variables[index][1][d], variables1)
            if index + 1 < len(variables1):
                variables1[index + 1][1] = is_forward_way(copy.deepcopy(variables1), index + 1)
            forwardchecking_algorithm(variables1, index + 1, accumulator)

    return accumulator


def print_result(results):
    chessboards = list()
    for el in results:
        size = len(el)
        chessboard = list()
        for x in range(0, size):
            column = list()
            for y in range(0, size):
                if el[x][0] == y:
                    column.append('X')
                else:
                    column.append('-')
            chessboard.append(column)
        pprint(chessboard)
        print("")
        chessboards.append(chessboard)


# size - size of chessboard
# Methods: 'b' - backtraking, 'f' - forwardchecking
def find_solutions(size, method):
    variables = create_variables(size)
    print(variables)
    if method == 'b':
        result = backtracking_algorithm(variables, 0, [])
    if method == 'f':
        result = forwardchecking_algorithm(variables, 0, [])

    print("iteration number: " + str(COUNTER))
    print("Solutions number: " + str(len(result)))
    #print_result(result)
    #pprint(result)


# enter to the program
if __name__ == '__main__':
    size = 8  # size of chessboard
    method = 'f'  # 'b' - backtraking, 'f' - forwardchecking
    start_time = time.time()
    find_solutions(size, method)
    print("Execition time: " + str(time.time() - START_TIME))
