import math

top=int(input("Type in number #1: "))
bottom=int(input("Type in number #2: "))

if top == 0:
  print("Undefined")

elif top < 0 or bottom < 0:
  print ("in this house we stay positive! :D")

elif top == bottom:
  print ("Those are the same number, haha!")

else:
  if bottom > top:
    x=bottom*100/top
    print(x-100, "% increase")
  else:
    x=(top-bottom)*100/top
    print(x, "% decrease")