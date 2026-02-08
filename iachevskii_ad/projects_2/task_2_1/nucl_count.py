dna = input("Введите последовательность ДНК: ").upper()
count_A = dna.count("A")
count_T = dna.count("T")
count_G = dna.count("G")
count_nucle = len(dna)
percent_A=count_A/count_nucle*100
percent_T=count_T/count_nucle*100
percent_G=count_G/count_nucle*100
print("Подсчёт нуклеотидов:")
print(f"A: {count_A} ({percent_A}%)")
print(f"T: {count_T} ({percent_T}%)")
print(f"G: {count_G} ({percent_G}%)")
print(f"nucle: {count_nucle}")