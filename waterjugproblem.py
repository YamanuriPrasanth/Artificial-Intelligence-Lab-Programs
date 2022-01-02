print("water jug problem")
x=int(input("enter the capacity of jug 1"))
y=int(input("enter the capacity of jug 2"))
while True:
    rno=int(input("Enter rule number"))
    if rno==1:
        if x<=5:
            x=5
    if rno==2:
        if x>=5:
            x=0
    if rno==3:
        if y<=3:
            y=3
    if rno==4:
        if y>=3:
            y=0
    if rno==5:
        if x+y<5 and y>0:
            x,y=x+y,0
    if rno==6:
        if x+y>5 and y>0:
            x,y=5,y-(5-x)
    if rno==7:
        if x+y<=3 and x>0:
            x,y=0,x+y
    if rno==8:
        if x+y>3 and x>0:
            x,y=x-(3-y),3
    if x==4:
        print("Goal Reached")
        break 