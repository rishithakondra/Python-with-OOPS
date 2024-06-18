class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def speak(self,hobbie):
        print(f"Hi my name is {self.name} and my age is {self.age} and my hobbie is {hobbie} " )
ris=Person("rishi","19")
ris.speak("playing")
