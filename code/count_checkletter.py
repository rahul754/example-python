user = input(">")
chars = ['a','b','c','d']

howmany = []
for char in chars:
    a = user.count(char)
    howmany.append(a)

print("a : ",str(howmany[0]),'b: '+str(howmany[1]),'c: '+str(howmany[2]),'d: '+str(howmany[3]))
