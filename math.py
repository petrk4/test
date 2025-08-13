from random import randint
def show_moves(moves): #показывает список комманд
    print("-" * 20)
    for k, v in moves.items():
        print(f"{k}. {v}")
    print("-" * 20)

def av_val(spisok):
    a = 0
    for i in spisok:
        a+=i
    print(a / len(spisok))

def bin_search(spisok):
    srt_sp = []
    srt_sp = sorted(spisok)
    print("max: ", srt_sp[-1], " min: ", srt_sp[0])

def sort_sp(spisok):
    print("По возрастанию:", *sorted(spisok))
    print("По убыванию:", *list(reversed(sorted(spisok))))

def deg():
    a = int(input("Введите число, которое хотите возвести в степень: "))
    while type(a) != int:
        a = int(input("Это не число, попробуйте ещё раз: "))
    d = int(input("Введите степень, в которую хотите возвести число: "))
    while type(d) != int:
        d = int(input("Это не степень, попробуйте ещё раз: "))
    print(a**d)

def mas_filling():
    print("ВЫБЕРИТЕ ЗАПОЛНЕНИЕ МАССИВА")
    mov = {
        1: "Заполнить массив вручную",
        2: "Заполнить массив случайно.",
    }
    show_moves(mov)
    a = int(input("Выберите команду: "))
    while a not in mov.keys():
        a = int(input("Такой команды не существует, попробуйте ещё раз: "))
    spisok = []

    if a == 1:
        x = int(input("Введите длину массива: "))
        while type(x) != int:
            x = int(input("Это не число, попробуйте ещё раз: "))
        for i in range(x):
            el = int(input(f"Введите {i+1} элемент массива: "))
            spisok.append(el)
    if a == 2:
        x = int(input("Введите длину массива: "))
        while type(x) != int:
            x = int(input("Это не число, попробуйте ещё раз: "))
        for i in range(x):
            spisok.append(randint(-10, 10))
    print("Ваш массив:", *spisok)
    return spisok

if __name__ == '__main__':
    moves = {
        1: "Вычисление среднего значения списка чисел.",
        2: "Поиск максимального и минимального числа в списке.",
        3: "Сортировка списка чисел по возрастанию или убыванию.",
        4: "Возведение чисел в степень.",
        5: "Поменять массив",
        6: "Показать список команд ещё раз.",
        7: "Выйти."
    }
    spisok = mas_filling()
    show_moves(moves)
    while True:
        a = int(input("Выберите команду: "))
        while a not in moves.keys():
            a = int(input("Такой команды не существует, попробуйте ещё раз: "))
        if a == 1:
            av_val(spisok)
        if a == 2:
            bin_search(spisok)
        if a == 3:
            sort_sp(spisok)
        if a == 4:
            deg()
        if a == 5:
            spisok = mas_filling()
        if a == 6:
            show_moves(moves)
        if a == 7:
            print("Программа завершена!")
            break