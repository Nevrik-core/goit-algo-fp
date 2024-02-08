items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):

    # Створюємо список (назва, співвідношення калорій до вартості, вартість, калорії) для кожного предмета
    item_list = [(item, value['calories'] / value['cost'], value['cost'], value['calories']) for item, value in items.items()]

    # Сортуємо список за співвідношенням калорій до вартості в спадному порядку
    item_list.sort(key=lambda x: x[1], reverse=True)

    total_calories = 0
    chosen_items = []

    for item, _, cost, calories in item_list:
        if budget - cost >= 0:  # Якщо можемо дозволити собі цю страву в рамках бюджету
            budget -= cost  # Віднімаємо вартість страви від бюджету
            total_calories += calories  # Додаємо калорії від цієї страви
            chosen_items.append(item)  # Додаємо страву до списку вибраних

    return chosen_items, total_calories


def dynamic_programming(items, budget):

    # Перетворення словника items у список кортежів (назва, вартість, калорійність)
    item_list = [(name, value['cost'], value['calories']) for name, value in items.items()]

    n = len(item_list) # Кількість предметів

    # Ініціалізуємо таблицю динамічного програмування
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    # Побудова таблиці dp від [0][0] до [n][budget]
    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            cost, calories = item_list[i-1][1], item_list[i-1][2]
            if cost <= w:
                dp[i][w] = max(calories + dp[i-1][w-cost], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    # Відновлення вибору: знаходимо, які предмети були включені в оптимальний набір
    chosen_items = []
    w = budget
    for i in range(n, 0, -1):

        # Якщо значення в dp[i][w] відрізняється від dp[i-1][w], це означає, що предмет був включений
        if dp[i][w] != dp[i-1][w]:
            chosen_items.append(item_list[i-1][0])
            w -= item_list[i-1][1]

    return chosen_items, dp[n][budget]



budget = 100
greedy_selection, greedy_calories = greedy_algorithm(items, budget)
dynamic_selection, dynamic_calories = dynamic_programming(items, budget)

print("Вибір жадібного алгоритму:", greedy_selection)
print("Загальна калорійність (Жадібний алгоритм):", greedy_calories)

print("\nВибір динамічного програмування:", dynamic_selection)
print("Загальна калорійність (Динамічне програмування):", dynamic_calories)

