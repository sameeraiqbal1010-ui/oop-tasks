class Bird:
    def fly(self):
        print("Bird can fly")

class Penguin(Bird):
    def fly(self):
        print("Penguin can't fly")

def show_flying(bird):
    bird.fly()

show_flying(Bird())
show_flying(Penguin())