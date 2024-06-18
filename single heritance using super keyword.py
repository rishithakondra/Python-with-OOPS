class Parent:
    def func1(self):
        print("func 1")
class Child(Parent):
    def func2(Self):
        super().func1()
        print("func 2")
ob=Child()
ob.func2()