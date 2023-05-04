import random
char_lists=['a','b','c','d','e','f','g','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','u','w','x','y','z']
symboll_list=['@','#','$','^','&','*','(',')']
number_list=['1','2','3','4','5','6','7','8','9',]
char_amount=int(input("how many letter do you wanna to include in you password\n\t"))
symboll_amount=int(input("how many symboll do you wanna to include \n\t"))
number_amount=int(input("how many number do you wanna to include\n\t"))
passwordlist=[]
for char in range(0,char_amount):
    passwordlist.append(random.choice(char_lists))
for symbol in range(0,symboll_amount):
    passwordlist+=random.choice(symboll_list)
for number in range(0,number_amount):
    passwordlist+=random.choice(number_list)
passwordlist=random.shuffle(passwordlist)
print(passwordlist)   