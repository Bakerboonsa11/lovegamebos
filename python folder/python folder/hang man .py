import random
word_list = ["bilisummaa","walabummaa","gabrummaa"]
choosen_word = random.choice(word_list)
print(f" {choosen_word}")
display =[]
for letter in choosen_word:
    display+="_"
print(display)
end_of_game=False 
while not  end_of_game:
 guss = input("please guss the lettr \n\t") 
 for possition in range(len(choosen_word)):
    letter=choosen_word[possition]
    if letter==guss:
         display[possition]=letter
 print(display)
 if "_" not in display:
      end_of_game=True
      print("you won")


