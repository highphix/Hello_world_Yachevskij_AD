researcher_name = input("Введите ФИО исследователя: ")
experiment_date = input("Введите дату (дд.мм.гггг): ")
experiment_name = input("Введите название эксперимента: ")
conclusion = input("Введите вывод: ")
border = "+" + "-" * 104 + "+"
with open("journal.txt", "w", encoding="utf-8") as file:
    file.write(f"{border}\n")
    file.write(f"| {'Электронный лабораторный журнал'}\t*10|\n")
    file.write(f"{border}\n")
    file.write(f"| {'ФИО исследователя: ' + researcher_name}\t*10|\n")
    file.write(f"| {'Дата: ' + experiment_date}\t*15|\n")
    file.write(f"| {'Эксперимент: ' + experiment_name}\t*11|\n")
    file.write(f"{border}\n")
    file.write(f"| {'Вывод:' + conclusion}|\n")
    file.write(f"{border}\n")

print("Запись успешно сохранена в journal.txt")