from scipy.optimize import LinearConstraint
from scipy.optimize import milp
import numpy as np

def convert_to_int(state):
    result = 0
    for i in range(len(state)):
        result = result * 2 + (1 if state[i] == '#' else 0)
    return result

def get_min_button_presses(buttons, joltages):
    ''' 
        If x_1, x_2,.. x_m represent number of times each button has been pressed, we must satisfy
        i)  sum_{j = 1 to m} x_j * I[level i in button j] = joltages[i] 
        ii) x_j >= 0
    '''
    n = len(joltages)
    m = len(buttons)
    c = np.ones(m)
    lb = np.array(joltages + [0 for _ in range(m)])
    ub = np.array(joltages + [np.inf for _ in range(m)])
    A = np.zeros((n + m, m))

    for idx,button in enumerate(buttons):
        for val in button:
            A[val][idx] += 1
    for var in range(m):
        A[var + n][var] = 1
    constraints = LinearConstraint(A = A, lb = lb, ub = ub)
    integrality = np.ones_like(c)
    res = milp(c=c, constraints=constraints, integrality=integrality)
    return res.fun


with open("input.txt", 'r') as f:
    lines = f.readlines()
    buttons = [[eval(button) for button in line.split(' ')[1:-1]] for line in lines]
    buttons = [[(buttons[machine][button_num] ,) if type(buttons[machine][button_num]) is int else buttons[machine][button_num] for button_num in range(len(buttons[machine]))] for machine in range(len(buttons))]
    joltage_levels = [eval('[' + line.split(' ')[-1].strip()[1:-1] + ']') for line in lines]
    
    button_presses = 0

    for machine in range(len(joltage_levels)):
        button_presses += get_min_button_presses(buttons[machine], joltage_levels[machine])

    print(button_presses)
