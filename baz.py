from foo import Foo


class Baz:
    __foo: Foo

    def __init__(self):
        self.__foo = None

    def getFoo(self) -> Foo:
        return self.__foo

    def setFoo(self, foo: Foo) -> None:
        if self.__foo != foo:
            self.__foo = foo
            foo.addBaz(self)
