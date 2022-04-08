class Cat:
   def __init__(self):
      self.year = 3
      self.eats = 'many'
      self.signal_in_6am = 'very very good'
      self.motor_ = 'very good'
      self.jump = 'good'
      self.lazy = 'very'

   def eat(self):
       print('їсть')

   def sleep(self):
       print('спить')

   def play(self):
       print('грає')

   def signal(self):
       print('кричить')
   
   def motor(self):
       print('мурчить')

   def toilet(self):
       print('ходить в туалет')

my_cat = Cat()

my_cat.eat()
my_cat.sleep()
my_cat.play()
my_cat.signal()
my_cat.motor()
my_cat.toilet()

