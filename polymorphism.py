#polymorphism=one method inside the class
class Animal:
    def speak(Self):
        raise NotImplementedError("Subclasses must implement this method")
class Dog (Animal):
    def speak(self):
        return "Woof!"
class Cat (Animal):
    def speak(self):
        return "Meow!"
def make_animal_speak(animal:Animal):
    print(animal.speak())
dog=Dog()
cat=Cat()

make_animal_speak(dog)
make_animal_speak(cat)