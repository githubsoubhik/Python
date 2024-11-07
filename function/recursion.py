# when function call itself  .....It behaves like loop

def show(n):
    if(n== 0):
        return # just out of the function or stop the function
    print (n)
    show(n-1) # here call the function itself
    
    print("end") # showing the result of call stack print the end layer tmes


no = int(input("write a no: "))
show(no)

