spisok=[]#Наш список дел
def start_menu():
    print("-" * 10, "Добро пожаловать", "-" * 10)
    print("1 — Посмотреть все дела.")
    print("2 — Добавить новое дело.")
    print("3 — Удалить дело по его номеру или названию.")
    print("4 — Выйти из программы.")
def shadow_task(tasks):
    if len(tasks) == 0:
        print("Ваш список пуст")
    else:
        print("Ваши дела: ")
        for i , task in enumerate(tasks , 1):
            print(f"{i}.{task}")
def add_task(taskes):
    new_item=input("Введите новое дело: ")
    spisok.append(new_item)
    print(f"Дело {new_item} успешно добавлено!")
def delet(taskes):
    if len(taskes) ==0:
        print("Список пуст , нечего удалять!")
        return

    print("Каким способом вы хотите удалить?")
    print("1- по номеру")
    print("2- по точному названию")
    try:
        pp = int(input("Введите действие: "))
    except ValueError:
        print("Ошибка! Введите число 1 или 2.")
        return

    if pp==1:
        print(f"""Ваш список дел:
        {taskes}""")
        try:
            num= int(input("Введите номер того, что хотите удалить: "))
            index = num - 1
            removed = taskes.pop(index)
            print(f"Удалено дело {removed}")
            print("Ваш список дел" , taskes)
        except ValueError:
            print("Ошибка! Нужно было ввести номер цифрой.")
        except IndexError:
            print("Ошибка! Дела с таким номером нет в списке.")

    elif pp==2:
        print("Исходный список: " , taskes)
        task_name=input("Введите точное название дела, которое хотите удалить: ")
        if task_name in  taskes:
            taskes.remove(task_name)
            print("Оставшиеся дела:", taskes)
        else:
            print("Такого дела нету в списке!")
    else:
        print("Ошибка: введите только 1 или 2")










while True: #Откритие цикла
    start_menu()

    try:
        von = int(input("Сделайте выбор: "))
    except ValueError:
        print("Ошибка! Нужно было ввести число, а не буквы.")
        continue

    if von==1:
        shadow_task(spisok)
    elif von==2:
        add_task(spisok)
    elif von==3:
        delet(spisok)
    elif von==4:
        print("Досвидание!!!!")
        break
    else:
        print("Ошибка! Введите только 1, 2, 3 или 4")




