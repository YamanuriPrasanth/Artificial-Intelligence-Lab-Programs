Aim: Implementation of water jug problem

Program:
print("water jug problem")
x=int(input("Enter Initial value "))
y=int(input("Enter Initial value "))
while True:
    rno=int(input("Enter rule number "))
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
    print('X is:',x)
    print('Y is:',y)
    if x==4:
        print("Goal Reached")
        break 
        
Output:
water jug problem
Enter Initial value 0
Enter Initial value 0
Enter rule number 1
X is: 5
Y is: 0
Enter rule number 8
X is: 2
Y is: 3
Enter rule number 4
X is: 2
Y is: 0
Enter rule number 7
X is: 0
Y is: 2
Enter rule number 1
X is: 5
Y is: 2
Enter rule number 8
X is: 4
Y is: 3
Goal Reached    
    
    
