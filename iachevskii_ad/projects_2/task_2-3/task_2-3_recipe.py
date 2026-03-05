nutrient_medium = input("Введите название питательной среды: ")
agar_concentration = input("Введите концентрацию агара (%): ")
sterilization_temperature = input("Введите температуру стерилизации (°C): ")
with open("recipe.txt", "w", encoding="utf-8") as recipe:
 recipe.write(f"{nutrient_medium}\n")
 recipe.write(f"{agar_concentration}\n{sterilization_temperature}\n")
 print("Файл 'recipe.txt' успешно сформирован!")