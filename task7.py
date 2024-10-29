from tabulate import tabulate
from random import randint

def throw_dices():
    return randint(1, 6), randint(1, 6)

def calculate_dices_results(attempts = 1000):
    results = dict.fromkeys(range(2, 13), 0)

    while attempts > 0:
        num1, num2 = throw_dices()
        results[num1+num2] += 1
        attempts -= 1

    return results

if __name__ == "__main__":
    attempts = 99999999
    results = calculate_dices_results(attempts)

    data = [[k,f'{v/attempts:.2%} {round(v/attempts*36)}/36'] for k,v in results.items()]

    print(tabulate(data, headers=['Сума', 'Ймовірність'], tablefmt='fancy_grid'))
