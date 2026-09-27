spisok=[]# список дел

while True:  # начало цыкла
    print("1 — Посмотреть все дела.")
    print("2 — Добавить новое дело.")
    print("3 — Удалить дело по его номеру или названию.")
    print("4 — Выйти из программы.")
    von=int(input("Сделайте выбор: "))
    if von==1:  # показ списка дел
        if len(spisok) == 0:
            print("Ваш список дел пока пуст!")
        else:
            for i in spisok:
                print(f"- {i}")
    elif von==2: # добавить дело в список spisok
        new_item = input("Введите новый список: ")
        spisok.append(new_item)
    elif von==3: # удалить дело по индексу или названию spisok
        print("Каким способом вы хотите удалить?")
        print("1- по номеру")
        print("2- по точному названию")
        pp=int(input("Введите действие: "))
        if pp==1: # индекс удедаление spisok
            print("Исходный список: ", spisok)
            num = int(input("Введите индекс того что хотите удалить: "))
            index = num - 1
            spisok.pop(index)
            print("Оставшиешся дела: ", spisok)
        elif pp==2: # удаление по названию spisok
            print("Исходный список: ", spisok)
            task_name=input("Введите точное название дела, которое хотите удалить: ")
            spisok.remove(task_name)
            print("Оставшиеся дела:", spisok)
        else:
            print("Ошибка введите только 1 или 2")
    elif von==4: # выход из цыкла
        print("Досвидание!!!!")
        break
    else: # если вели число больше 4
        print("Ошибка введите только 1 , 2 , 3 или 4")
