import random
memmbers=input("enter all of your name, sepparedted by comma")
name = memmbers.split(", ")
number_ofmember=len(name)
choice=random.randint(0, number_ofmember-1)
random_choice=name[choice]
print( f"{random_choice}is going to pay")

