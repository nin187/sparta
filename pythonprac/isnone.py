class Foo:
    def __eq__(self, other):
        return True


foo = Foo()

print(foo == None)
# True

print(foo is None)
# False