class Animal:
    def _init_(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def sound(self):
        print(f"{self.name} barks")

d = Dog("Buddy")
d.sound()