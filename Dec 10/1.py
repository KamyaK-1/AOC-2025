from functools import reduce
def convert_to_int(state):
    result = 0
    for i in range(len(state)):
        result = result * 2 + (1 if state[i] == '#' else 0)
    return result

def get_min_button_presses(buttons, final_state, lights_count):
    visited = [False] * (1 << lights_count)
    queue = [0]
    visited[0] = True
    num_switches = 0

    while queue:
        new_states_found = []
        for state in queue:
            if state == final_state:
                return num_switches
            for button in buttons:
                new_state = state ^ button
                if visited[new_state] == False:
                    new_states_found.append(new_state)
                    visited[new_state] = True
        queue = new_states_found
        num_switches += 1
    assert False
    

with open("input.txt", 'r') as f:
    lines = f.readlines()
    final_states = [line.split(' ')[0] for line in lines]
    lights_count = [len(state) - 2 for state in final_states]
    final_states = [convert_to_int(state[-2:0:-1]) for state in final_states]
    buttons = [[eval(button) for button in line.split(' ')[1:-1]] for line in lines]
    buttons = [[(buttons[machine][button_num] ,) if type(buttons[machine][button_num]) is int else buttons[machine][button_num] for button_num in range(len(buttons[machine]))] for machine in range(len(buttons))]
    buttons = [[reduce(lambda x,y : x + y, map(lambda x : 1 << x , buttons[machine][button_num])) for button_num in range(len(buttons[machine]))] for machine in range(len(buttons))]
    
    button_presses = 0
        
    for machine in range(len(buttons)):
        button_presses += get_min_button_presses(buttons[machine], final_states[machine], lights_count[machine])

    print(button_presses)
