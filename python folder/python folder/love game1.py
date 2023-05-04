print("\n\ti will calculate how much your  love is ")
name_guy=input('enter the name of "NUGUSE"\n\t')
name_you=input('enter the name of "NIGIST"\n\t')
full_name=name_guy +name_you
full_name.lower()
t=int(full_name.count('t'))
r=int(full_name.count('r'))
u=int(full_name.count('u'))
e=int(full_name.count('e'))
total_true=t+r+u+e
total_truestr= str(total_true)

l=int(full_name.count('l'))
o=int(full_name.count('o'))
v=int(full_name.count('v'))
e=int(full_name.count('e'))
total_love=l+o+v+e
total_lovestr=str(total_love)
love_percent=total_truestr+total_lovestr

if int(love_percent) <= 20:
    print(f"true love percent  = {love_percent}%  \n\t so you have to break it right know")
elif int(love_percent) <= 50:
    print(f"love percent  = {love_percent}% \n\t so you have to try continue as much as you can")
elif int(love_percent) <= 80:
    print(f"true love percent = ,{love_percent}%  \n\t wow so happy situation keep it up an try to sty forever with heir")
else:
    print(f"  your love percent = {love_percent}% \n\t wow! wow! and wow! unbelivable// so so perfect love  marry heir now! now!!!!!!! ")

