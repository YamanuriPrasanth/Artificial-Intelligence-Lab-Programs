def TowerOfHanoi(n , source1, destination, auxiliary):
    if n==1:
        print("Move disk 1 from source",source1,"to destination",destination)
        return
    TowerOfHanoi(n-1, source1, auxiliary, destination)
    print("Move disk",n,"from source",source1,"to destination",destination)
    TowerOfHanoi(n-1, auxiliary, destination, source1)
          

n = 4
TowerOfHanoi(n,'A','B','C') 