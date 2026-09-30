spisok=[]# список дел

while True:  # начало цыкла
    print("-"* 10 , "Добро пожаловать" , "-" *10)
    print("1 — Посмотреть все дела.")
    print("2 — Добавить новое дело.")
    print("3 — Удалить дело по его номеру или названию.")
    print("4 — Выйти из программы.")
    try:
        von=int(input("Сделайте выбор: "))
    except ValueError:
        print("Ошибка! Нужно было ввести число, а не буквы.")
        continue
    if von==1:  # показ списка дел
        if len(spisok) == 0:
            print("Ваш список дел пока пуст!")
        else:
            for i in spisok:
                print(f"- {i}")
    elif von==2: # добавить дело в список spisok
        new_item = input("Введите новое дело: ")
        spisok.append(new_item)
    elif von==3: # удалить дело по индексу или названию spisok
        print("Каким способом вы хотите удалить?")
        print("1- по номеру")
        print("2- по точному названию")
        try:
            pp=int(input("Введите действие: "))
        except ValueError:
            continue

        if pp==1: # индекс удедаление spisok
            print("Исходный список: ", spisok)
            try:
                num = int(input("Введите индекс того что хотите удалить: "))
                index = num - 1
                spisok.pop(index)
                print("Оставшиешся дела: ", spisok)
            except ValueError:
                print("Введите номер заданния!!!")
            except IndexError:
                print("Ошибка! Дела с таким номером нет в списке.")
                continue
        elif pp==2: # удаление по названию spisok
            print("Исходный список: ", spisok)
            task_name=input("Введите точное название дела, которое хотите удалить: ")
            if task_name in spisok:
                spisok.remove(task_name)
                print("Оставшиеся дела:", spisok)
            else:
                print("Такого дела нету в списке!")
        else:
            print("Ошибка введите только 1 или 2")
    elif von==4: # выход из цыкла
        print("Досвидание!!!!")
        break
    else: # если вели число больше 4
        print("Ошибка введите только 1 , 2 , 3 или 4")
