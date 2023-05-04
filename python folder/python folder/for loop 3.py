def risepower ( base,power):
    result  = 1
    for i in range(power):
        result=result*base
    return result


base = int(input("please enter the base "))
power = int(input("plese enter the the exponent "))
    


print(risepower(base, power)) 