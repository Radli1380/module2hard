def find_number_pairs(number):
    pairs = []
    for i in range(1, number):
        for j in range(i+1, number):
            if i + j == number:
                pairs.append((i, j))
    return pairs
number = int(input("Введите число от 3 до 20: "))
pairs = find_number_pairs(number)
if pairs:
    print(f"Возможные пары чисел для числа {number}:")
    for pair in pairs:
        print(pair[0], pair[1])
else:
    print("Для данного числа нет подходящих пар чисел.")
