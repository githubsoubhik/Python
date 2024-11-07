def factorial(n):
    fno=1
    for i in range(1, n+1) :
        #print("fno")
        fno=fno*i
    
    print(fno)

 
no=int(input("input the no: "))
factorial(no)