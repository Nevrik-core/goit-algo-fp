import turtle

def draw_branch(t, branch_length, order):
    if order == 0:
        return

    # Малюємо основну гілку
    t.forward(branch_length)
    # Створюємо нові гілки під кутами 45 та -45 градусів
    t.left(45)
    draw_branch(t, branch_length / (2 ** 0.5), order - 1)
    t.right(90)
    draw_branch(t, branch_length / (2 ** 0.5), order - 1)
    t.left(45)
    # Повертаємося до початку гілки
    t.backward(branch_length)

def setup_turtle():
    window = turtle.Screen()
    window.bgcolor("white")
    t = turtle.Turtle()
    t.speed('fastest')
    t.penup()
    t.color("red")
    t.goto(0, -window.window_height() / 4)
    t.pendown()
    t.left(90)
    return t, window

def main():
    recursion_level = int(input("Введіть рівень рекурсії для дерева Піфагора: "))
    size = 150
    t, window = setup_turtle()
    draw_branch(t, size, recursion_level)
    window.exitonclick()

main()
