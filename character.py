

# name
# avatar (profile pic)
# inventory

# def do_stuff():
#     pass
# class used like def and is capitalized
class Character():
    # "dunder init" method is constructor (double underscore init)
    def __init__(self, new_name, new_avatar):
        #  `self` is the customary way to refer to instance being built
        #  in some other languages, they use `this`
        self.name = new_name
        self.avatar = new_avatar
        self.inventory = []

        # `someone=None` is default argument
        #`None` is equivalent to `Null` in other languages
    def greet(self, someone = None):
        # We assume that `someone` argument has a `.name` property
        # this is an Object-Oriented Programming principle
        # polymorphism
        # if it walks ,talks, acts like a duck. it is a duck
        # ^ "Duck Typing" in python

        if someone is not None:
            return "Hello, %s I am %s. I am awesome. " % (someone.name, self.name)
        else:
            return "Hello, I am %s. I am awesome. " % (self.name,)
    def attack(self, someone= None):
        if someone is Monster(Character):
            return "%s has slain %s" % (self.name, someone.name)
        else:
            return "%s refuses to attack and can only attack Monsters" % (self.name)

# Hero is a kind of Character
# Hero is still subclass of Character
# Hero inherits from Character
# Character is the superclass of Hero
class Hero(Character):
    pass

class Monster(Character):
    def __init__(self):
        pass
    def greet(self):
        return "ugggh"

