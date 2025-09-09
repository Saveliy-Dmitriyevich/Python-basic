memory_action = []

def add(num_1, num_2):
    return num_1 + num_2
def subtract(num_1, num_2):
    return num_1 - num_2
def multiply(num_1, num_2):
    return num_1 * num_2
def divide(num_1, num_2):
    return num_1 / num_2
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
        num = input('Enter your number ')
        try:
            return float(num)
        except ValueError:
            print("Invalid number, try again")
def memory(num_1, num_2, final_result):
    memory_action.append(f'{num_1} {action} {num_2} = {final_result} ')
def memory_another(num_1, final_result):
    memory_action.append(f'{action} {num_1} = {final_result} ')
def memory_print():
    print(*memory_action, sep="\n")

action_list = ['add', 'subtract', 'multiply', 'divide', 'quit', 'memory', 'sqrt', 'square','cube', 'mod']
action = ''
while action != 'quit':
    print()
    print(*action_list)
    action = input('What would you like to do? ').strip().lower()
    if action == 'quit':
        print('Thank you for using this program. Goodbye!')
        break
    elif action == 'sqrt':
        num_1 = get_number()
        final_result = sqrt(num_1)
        print(f'result = {final_result}')
        memory_another(num_1, final_result)
    elif action == 'square':
        num_1 = get_number()
        final_result = square(num_1)
        print(f'result = {final_result}')
        memory_another(num_1, final_result)
    elif action == 'cube':
        num_1 = get_number()
        final_result = cube(num_1)
        print(f'result = {final_result}')
        memory_another(num_1, final_result)
    elif action == 'memory':
        memory_print()
    elif action not in action_list:
        print('Invalid action')
    else:
        num_1 = get_number()
        num_2 = get_number()
        if action == 'add':
            final_result =  add(num_1, num_2)
            print(f'result = {final_result}')
            memory(num_1, num_2, final_result)
        elif action == 'subtract':
            final_result = subtract(num_1, num_2)
            print(f'result = {final_result}')
            memory(num_1, num_2, final_result)
        elif action == 'multiply':
            final_result = multiply(num_1, num_2)
            print(f'result = {final_result}')
            memory(num_1, num_2, final_result)
        elif action == 'mod':
            final_result = mod(num_1, num_2)
            print(f'result = {final_result}')
            memory(num_1, num_2, final_result)
        elif action == 'divide':
            if num_2 == 0:
                print('Division by zero')
            else:
                final_result = divide(num_1, num_2)
                print(f'result = {final_result}')
                memory(num_1, num_2, final_result)


