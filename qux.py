from foo import Foo


class Qux(Foo):
    def __init__(self, something: int):
        super().__init__(something)

    def doSomething(self):
        print("Je fais un truc à la mode Qux")
