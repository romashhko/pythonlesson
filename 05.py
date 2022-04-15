class baseCat:
 def __init__(self, name, color, dateBirthDay):
        self.name = name
        self.color = color
        self.dateBirthDay = dateBirthDay


class Cat1(baseCat):
    def __init__(self, name, color, dateBirthDay, breed):
        baseCat.__init__(self, name, color, dateBirthDay)

        self.breed = breed

class Cat2(baseCat):
    pass


tom_cat = Cat1('tom', 'red', '23.10.2019', 'бомбейська')

print(tom_cat.name)
print(tom_cat.color)
print(tom_cat.dateBirthDay)
print(tom_cat.breed)