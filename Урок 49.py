class Bank:
    def __init__(self , name , balance):
        self.name = name

        self.balance = balance

    def deposit(self , summa):
        if summa > 0:
            self.balance += summa
            return f"Баланс пополнен на {summa} руб!"
        else:
            return "Ошибка: положите больше '0' руб"

    def deposit2(self , summa):
        if summa <=0:
            return "Ошибка: введите больше '0' руб"

        elif summa > self.balance:
            return "Ошибка: недостаточно средств"

        else:
            self.balance -= summa
            return f"Успешно снято {summa} руб"

har = Bank("Vasya" , 1000)
print(har.deposit(360))

print(har.deposit2(1340))



