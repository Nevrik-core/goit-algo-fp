import numpy as np
import matplotlib.pyplot as plt

# Функція для симуляції кидків двох кубиків

def simulate_dice_rolls(num_rolls):
    # Генерація випадкових кидків для двох кубиків
    dice1 = np.random.randint(1, 7, num_rolls)
    dice2 = np.random.randint(1, 7, num_rolls)
    sums = dice1 + dice2

    # Підрахунок кількості кожної можливої суми
    counts = np.bincount(sums, minlength=13)[2:]  # Починаємо з індексу 2, тому що мінімальна сума - 2
    return counts


# Перетворення кількостей на ймовірності
def calculate_probabilities(counts, num_rolls):
    probabilities = counts / num_rolls
    return probabilities

# Кількість кидків
num_rolls = 100000
counts = simulate_dice_rolls(num_rolls)
probabilities = calculate_probabilities(counts, num_rolls)

# Виведення результатів
print(f"{'Сума':^5} {'Кількість':^10} {'Ймовірність':>12}")
print("-" * 28)
for total in range(2, 13):
    print(f"{total:^5} {counts[total-2]:^10} {probabilities[total-2]:>10.2%}")


# Побудова графіка
plt.bar(range(2, 13), probabilities)
plt.xlabel('Сума кубиків')
plt.ylabel('Ймовірність')
plt.title('Ймовірності сум кубиків за методом Монте-Карло')
plt.xticks(range(2, 13))
plt.show()
