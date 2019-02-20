# these are not real tests
from character import Character
# characters can be instantiated with name and avatar

arya = Character("Arya Stark","arya.png" )

jon = Character("Jon Snow", "jon.png")

print(arya.name, arya.avatar)
print(jon.name, jon.avatar)

# after adding 2 items to inventory
# length of inventory should == 2

arya.inventory.append('sword')
arya.inventory.append('mask')

print(len(arya.inventory))

# arya should have  a`greet` method
# when called, it should return:
# "Hello, I am Arya Stark. I am awesome."
print(arya.greet())