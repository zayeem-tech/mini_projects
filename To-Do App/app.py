def task():
    tasks = []
    print('=====WELCOME TO THE TASK MANAGEMENT APP=====')

    total_task = int(input('Enter the number of tasks you want add: '))

    for i in range(total_task):
        task_name = input(f'Enter task {i+1}: ')
        tasks.append(task_name)

    print(f'Today\'s tasks are\n{tasks}')
    while True:
        operation = int(input('Enter action: \n1-Add\n2-Update\n3-Delete\n4-Exit/Stop\n'))
        match operation:
            case 1:
                add = input('Enter task you want to add: ')
                tasks.append(add)
                print('Task added!')
                print(f'Today\'s tasks are\n{tasks}')
            case 2:
                updated_val = input(
                    'Enter the task name you want to update: ')
                if updated_val in tasks:
                    up = input('Enter new task: ')
                    ind = tasks.index(updated_val)
                    tasks[ind] = up
                    print('Task Updated!')
                    print(f'Today\'s tasks are\n{tasks}')
                else:
                    print('\nThe task you entered is not present in to-do list\n')

task()