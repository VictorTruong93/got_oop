

# name
# avatar (profile pic)
# inventory

# def do_stuff():
#     pass
# class used like def and is capitalized
class Character():
    # "dunder init" method is constructor (double underscore init)
    def __init__(self, new_name, new_avatar):
#        #  `self` is the customary way to refer to instance being built
#       #  in some other languages, they use `this`
        self.name = new_name
        self.avatar = new_avatar
        self.inventory = []