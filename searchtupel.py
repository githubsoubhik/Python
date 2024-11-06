# search the x in this tuple

# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

x= int(input("write search no : "))


tuplenos= (1, 4, 9, 16, 25, 36, 49, 4, 16, 64, 81,100)

idx= 0
for el in tuplenos :
    if el== x:
      print (el,"found in position ", idx)
    idx+=1
