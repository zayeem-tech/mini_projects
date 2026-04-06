import random
import time

OPERATORS = ['+', '-', '*']
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10


def generateProblem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expression = str(left) + ' ' + operator + ' ' + str(right)
    answer = eval(expression)
    return expression, answer


correct_count = 0
input('Press enter to start.')
print()
start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expression, answer = generateProblem()
    while True:
        guess = input(f'Problem {i+1} : {expression} = ')
        if guess == str(answer):
            correct_count += 1
            print(' - Correct -')
            break
        else:
            print(' - Wrong -')

end_time = time.time()
time_taken = end_time-start_time
print(f'\n You finished in {time_taken:.1f} seconds.')
