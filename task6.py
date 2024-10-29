import numpy as np

def greedy_algorithm(items, cost_limit):
    menu = set()
    calories = 0
    for food, food_data in sorted(items.items(), key=lambda item: item[1]['calories'], reverse=True):
        if food_data['cost'] < cost_limit:
            menu.add(food)
            cost_limit -= food_data['cost']
            calories += food_data['calories']

    return {
        'menu': menu,
        'calories': calories
    }

def dynamic_programming(food, cost_limit):
    food_items = [{'name': name, **data} for name, data in sorted(food.items(), key=lambda item: item[1]['cost'])]
    table = [[0 for w in range(cost_limit + 1)] for i in range(len(food_items) + 1)]

    for i in range(len(food_items) + 1):
        for w in range(cost_limit + 1):
            if i == 0 or w == 0:
                table[i][w] = 0
            elif food_items[i - 1]['cost'] <= w and food_items[i - 1]['calories'] + table[i - 1][w - food_items[i - 1]['cost']] > table[i - 1][w]:
                table[i][w] = food_items[i - 1]['calories'] + table[i - 1][w - food_items[i - 1]['cost']]
            else:
                table[i][w] = table[i - 1][w]

    print(np.matrix(table))

    return table[-1][-1]

if __name__ == "__main__":
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 360},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    cost_limit = int(input('Enter max cost: '))
    print(greedy_algorithm(items, cost_limit))
    print(dynamic_programming(items, cost_limit))