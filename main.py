#mdowemfownlkwnref
def show_moves(moves): #показывает список комманд
    print("-" * 20)
    for k, v in moves.items():
        print(f"{k}. {v}")
    print("-" * 20)

def add_duty(duties): #добавляет задачу
    print("-" * 20)
    lst_duties = []
    for k in duties.keys():
        lst_duties.append(k)
    for i in range(1, len(duties) + 2):
        if i not in lst_duties:
            key = i
    name = input("Опишите задачу, которую хотите добавить: ")
    duties[key] = name + "(не выполнено)"
    print(f"Задача ({name}) была добавлена в список")
    print("-" * 20)
    print("ЧТОБЫ ПОСМОТРЕТЬ СПИСОК КОМАНД, НАЖМИТЕ 5")

def show_duties(duties): #показывает текущие задачи
    print("-" * 20)
    print("СПИСОК ТЕКУЩИХ ЗАДАЧ")
    for k, v in duties.items():
        print(f"{k}: {v}")
    print("-" * 20)
    print("ЧТОБЫ ПОСМОТРЕТЬ СПИСОК КОМАНД, НАЖМИТЕ 5")

def delete_duty(duties): #удаляет выбранную задачу
    print("-" * 20)
    num_of_duty = int(input("Напишите номер задачи, которую хотите удалить: "))
    while num_of_duty not in duties.keys():
        num_of_duty = int(input("Такой задачи не существует, попробуйте ещё раз: "))
    del duties[num_of_duty]
    print(f"Задача под номером {num_of_duty} удалена")
    print("-" * 20)
    print("ЧТОБЫ ПОСМОТРЕТЬ СПИСОК КОМАНД, НАЖМИТЕ 5")

def mark_duty_completed(duties): #отмечает задачу как выполненную
    print("-" * 20)
    num_of_duty = int(input("Выберите номер задачи, которую хотите отметить как выполненную: "))
    while num_of_duty not in duties.keys():
        num_of_duty = int(input("Такой задачи не существует, попробуйте ещё раз: "))
    name_of_duty = duties[num_of_duty]
    if "(не выполнено)" in name_of_duty:
        name_of_duty = name_of_duty[:-14] + "(выполнено)"
        duties[num_of_duty] = name_of_duty
        print(f"Задча под номером {num_of_duty}({name_of_duty[:-11]}) теперь выполнена!")
    else:
        print("Эта задача уже выполнена!")
    print("-" * 20)
    print("ЧТОБЫ ПОСМОТРЕТЬ СПИСОК КОМАНД, НАЖМИТЕ 5")

if __name__ == '__main__':
    moves = {
        1: "Добавить новую задачу в список",
        2: "Просмотр всех задач с их статусами (выполнена/не выполнена)",
        3: "Отметка задачи как выполненной",
        4: "Удаление задачи из списка",
        5: "Показать список команд ещё раз",
        6: "Выйти"
    }
    duties = {
        1: "Приготовить завтрак(не выполнено)",
        2: "Убраться(не выполнено)",
        3: "Сходить погулять(выполнено)",
        4: "Поиграть(выполнено)",
        5: "Поспать(не выполнено)"
    }
    show_moves(moves)
    while True:
        a = int(input("Введите номер пункта, в который хотите перейти: "))
        while a not in moves.keys():
            a = int(input("Такой команды не существует, попробуйте ещё раз: "))
        if a == 1:
            add_duty(duties)
        if a == 2:
            show_duties(duties)
        if a == 3:
            mark_duty_completed(duties)
        if a == 4:
            delete_duty(duties)
        if a == 5:
            show_moves(moves)
        if a == 6:
            print("Программа завершена!")
            break