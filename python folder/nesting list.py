# below line create each row separetly
row1=[" "," "," "]
row2=[" "," "," "]
row3=[" "," "," "]
mep=[row1,row2,row3]
style=f"{row1}\n{row2}\n{row3}"
print(style)
for chance in range(4):
  possitin=input(" mr .first player enter the possitin you wanna to pick")
  vertical=int(possitin[0])
  horizontal=int(possitin[1])
  mep[vertical-1][horizontal-1]="x"
  print(f"{row1}\n{row2}\n{row3}")
  
  possitin=input(" mr. 2nd player enter the possitin you wanna to pick")
  vertical=int(possitin[0])
  horizontal=int(possitin[1])
  mep[vertical-1][horizontal-1]="/"
  print(f"{row1}\n{row2}\n{row3}")
  
  

