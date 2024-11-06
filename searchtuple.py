#Search  for no x in this tuple using loop
# (1,4,9,16,25,35,45,55)

sno = int(input('write the searching no: '))

tuplenos= (1,4,9,16,25,35,45,55)

i=0

while (i<= len(tuplenos)-1):
    if tuplenos[i] == sno:
        print (i)

    i+=1