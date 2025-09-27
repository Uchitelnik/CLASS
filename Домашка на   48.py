#Напиши программу, которая проверяет будет ли число простым

ch = int(input("Введите число "))

def proverka(ch):
    if ch<2:
        print("Простое")
    for i in range (2, int(ch**0.5)+1):
        if ch % i == 0:
            return "составное"
    return "простое"
print(proverka(ch))
