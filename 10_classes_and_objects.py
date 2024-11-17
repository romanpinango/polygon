class Person:
    def __init__(self, _name, _surname, _city, _gender, _yob = 0, _nationality = None):
        self.name = _name
        self.surname = _surname
        self.city = _city
        self.gender = _gender
        self.year_of_birth = int(_yob)
        self.nationality = _nationality
        self.hair_color = "brown"
        if self.year_of_birth < 2000:
            self.age = None
        else:
            self.age = 2024 - self.year_of_birth

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_full_name_in_french(self):
        return self.surname.upper() + ", " + self.name


class Product:
    def __init__(self, _price):
        self.price = _price

    def get_price_with_discount(self):
        return self.price * 0.90


p_1 = Person("Francisco", "Castillo", "Orlando", "M")
print(p_1.get_full_name_in_french())
print(p_1.year_of_birth)
print(p_1.age)

prod_1 = Product(150)
print(prod_1.price)
print(prod_1.get_price_with_discount())

list_of_persons = []

with open("data.txt", "r") as file:
    for line in file:
        values = line.split(',')
        list_of_persons.append(Person(values[0], values[1], values[2], values[3], values[4], values[5]))

for p in list_of_persons:
    print(p.get_full_name_in_french())


#p_2 = Person("", "", "", "", 0, "", ["Roman", "Piñango"])
#print(p_2.get_full_name())

