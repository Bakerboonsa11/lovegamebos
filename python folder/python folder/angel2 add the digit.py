name = input("please enter a two digit  number \n\t")
num_1=name[0]
num_2=name[1]
result =int(num_1)+int(num_2)
print("the sum of the digit is \n\t" + str(result))
weight = input("please ebter your weight\n\t")
weight=int(weight)
height=input("please enter your height\n\t")
height=float(height)
bmi=weight/(height**2)
print("your bmi is " + str(bmi))