Aim: Implementation of Towers of Hanoi Problem

Program:
def TowerOfHanoi(n , source1, destination, auxiliary):
    if n==1:
        print("Move disk 1 from source",source1,"to destination",destination)
        return
    TowerOfHanoi(n-1, source1, auxiliary, destination)
    print("Move disk",n,"from source",source1,"to destination",destination)
    TowerOfHanoi(n-1, auxiliary, destination, source1)
n = 4
TowerOfHanoi(n,'A','B','C') 

Output:
Move disk 1 from source A to destination C
Move disk 2 from source A to destination B
Move disk 1 from source C to destination B
Move disk 3 from source A to destination C
Move disk 1 from source B to destination A
Move disk 2 from source B to destination C
Move disk 1 from source A to destination C
Move disk 4 from source A to destination B
Move disk 1 from source C to destination B
Move disk 2 from source C to destination A
Move disk 1 from source B to destination A
Move disk 3 from source C to destination B
Move disk 1 from source A to destination C
Move disk 2 from source A to destination B
Move disk 1 from source C to destination B    
