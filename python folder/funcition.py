def call_name(name,age):
   print("hello mr." +name+ " you are " +str(age) ) 
    
    
call_name("abdulkadir", 35)  
call_name("baker",44)

#return stetement
def cube(num):
    return num*num*num
print(cube(4))

#if statement
is_male=True
is_tall=True
if is_male and is_tall:
    print("you are male and short")

else:
    print("you are either short or femeale ") 
    
     
#if stetement with funcition and comparisio
def max (num1 ,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2 >=num1 and num2>=num3:
        return num2
    else:
        return num3
num1=input("enter the first number ")
num2=input("enter the 2nd number ")
num3=input("enter the thrd number ")
int(num1)
int(num2)
int(3)
print(max(num1, num2, num3))
    
    
      

