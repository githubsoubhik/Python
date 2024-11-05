#WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
#an empty dictionary & add one by one. Use subject name as key & marks as value.#


marks = {} #empty  dictionary

mks = int(input("Enter Physics No : "))

marks.update({"physic": mks})

mks = int(input("Enter Chemistry No : "))

marks.update({"Chemistry": mks})


mks = int(input("Enter Math No : "))

marks.update({"Math": mks})

print(marks)


