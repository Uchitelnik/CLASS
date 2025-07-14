class OOP:
    def __init__(self , name , age ):
        self.name = name
        self.age = age
        self.ocenki = []

    def DeSort(self , ocenka):
        self.ocenki.append(ocenka)

    def Uchitelnik(self):
        if not self.ocenki:
            return 0
        return sum(self.ocenki) / len(self.ocenki)


student = OOP("Petya" , 0.0000000000001)
student.DeSort(0.0000000001)
student.DeSort()
print(student.Uchitelnik())