from foo import Foo


class Corge(Foo):
    def __init__(self):
        super().__init__(23)

    def doSomething(self):
        print("Je fais un truc à la mode Corge")
