class Cat:
    def __init__(self, name, color, max_age, health):
        self.name = name
        self.color = color
        self.max_age = max_age
        self.health = health
        self.age = 0
        self.hunger = True
 

    def about(self):
        print("Ім'я кота : " + self.name)
        print("Його колір : " + self.color)
        print("Максимальний вік : " + str(self.max_age))
        print("Кількість життів: " + str(self.health)) 
        print('Вік кота:' + str(self.age))

    def HB(self):
        print('HB')
        self.age = self.age + 1

    def feed(self):
        if self.hunger:
          print('Кіт наївся...')
          self.hunger = False
        else:
            print('Негодуйте його, він ситий...')
  
    def run(self):
        if self.hunger:
            print('Кіт голодний,бігати не може, покорміть його')
        else:
            print('Кіт бігає...')
            self.hunger = True

    def sleep(self):
        print ('Кіт змучився, він лягає спати')
        self.hunger = True

    def get_up(self):
        print('Кіт прокинувся')