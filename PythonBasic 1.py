action_list = ['add', 'subtract', 'multiply', 'divide', 'quit']
action = ''
while action != 'quit':
    print()
    print(*action_list)
    action = input('What would you like to do? ')
    if action == 'quit':
        break
    if action not in action_list:
        print('Invalid action')
    else:
        num_1 = input('enter first number: ')
        if not num_1.isdigit():
            print('Invalid number 1')
            continue
        num_2 = input('enter second number: ')
        if not num_2.isdigit():
            print('Invalid number 2')
            continue

        num_1 = int(num_1)
        num_2 = int(num_2)

        if action == 'add':
            print('result = ', num_1 + num_2)
        elif action == 'subtract':
            print('result = ', num_1 - num_2)
        elif action == 'multiply':
            print('result = ', num_1 * num_2)
        elif action == 'divide':
            if num_2 == 0:
                print('Division by zero')
            else:
                print('result = ', num_1 / num_2)


