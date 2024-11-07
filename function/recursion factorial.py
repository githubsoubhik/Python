

# def recfac(n):
#     if(n==0 or n==1):
#         return 1
#     else: 
#         print(n * recfac(n-1))

# no= int(input("factorial: " ))

# recfac(no)

def recfac(n):
    if(n==0 or n==1):
        return 1
    else:
        return recfac(n-1)*n

recfac(4)

