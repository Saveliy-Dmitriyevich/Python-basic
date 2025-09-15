memory_action = []

def add(num_1, num_2):
    return num_1 + num_2
def subtract(num_1, num_2):
    return num_1 - num_2
def multiply(num_1, num_2):
    return num_1 * num_2
def divide(num_1, num_2):
    try:
        return num_1 / num_2
    except ZeroDivisionError:
        print("Division by zero, try again")
def square(num_1):
    return num_1 ** 2
def cube(num_1):
    return num_1 ** 3
def mod(num_1, num_2):
    return num_1 % num_2
def sqrt(num_1):
    return num_1 ** 0.5
def get_number():
    while True:
        num = input('Enter your number (or MR) ')
        if num.strip().upper() == "MR":
            return settings["memory"]
        try:
            return float(num)
        except ValueError:
            print("Invalid number, try again")
def precision():
    circle = int(input('Enter number of round '))
    settings['precision'] = circle
    print(f'number of round: {circle}')
settings ={
    "precision": 6,
    "memory": 0,
    "last_result": 0
}
def memory(num_1, num_2, final_result):
    memory_action.append(f'{num_1} {action} {num_2} = {round(final_result, settings['precision'])} ')
def memory_another(num_1, final_result):
    memory_action.append(f'{action} {num_1} = {round(final_result, settings['precision'])} ')
def memory_print():
    print(*memory_action, sep="\n")

operations = {
    "add": (add, 2 ),
    "subtract": (subtract, 2),
    "multiply": (multiply, 2),
    "divide": (divide, 2),
    "mod": (mod, 2),
    "sqrt": (sqrt, 1),
    "square": (square, 1),
    "cube": (cube, 1),
}

action_list = ['add', 'subtract', 'multiply', 'divide', 'quit', 'memory', 'sqrt', 'square','cube', 'mod', 'precision','M+','MR','MC']
action = ''

while action != 'quit':
    print()
    print(*action_list)
    action = input('What would you like to do? ').strip().lower()
    if action == 'quit':
        print('Thank you for using this program. Goodbye!')
        break
    elif action in operations:
        func, args = operations[action]
        if args == 1:
            num_1 = get_number()
            final_result = func(num_1)
            print(round(final_result, settings['precision']))
            settings['last_result'] = final_result
            memory_another(num_1, final_result)
        elif args == 2:
            num_1 = get_number()
            num_2 = get_number()
            final_result = func(num_1, num_2)
            print(round(final_result, settings['precision']))
            settings['last_result'] = final_result
            memory(num_1, num_2, final_result)
    elif action.strip().lower() == 'precision':
        precision()
    elif action.strip().lower() == 'memory':
        memory_print()
    elif action.strip().lower() == 'm+':
        settings['memory'] = settings['memory'] + settings['last_result']
    elif action.strip().lower() == 'mc':
        settings['memory'] = 0
        settings['last_result'] = 0
    elif action not in action_list:
        print('Invalid action')

