def task(class1, class2, class3):
    students = class1 + class2 + class3

    desk= (students + 1) // 2

    return desk

class1 = int(input("Кількість учнів у першому класі: "))
class2 = int(input("Кількість учнів у другому класі: "))
class3 = int(input("Кількість учнів у третьому класі: "))

desk= task (class1, class2, class3)
print("Загальна кількість потрібних парти: ", desk)
