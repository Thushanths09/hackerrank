if __name__ == '__main__':
    s = input("Enter:")

w=[]
n=[]
for se in s:
    if se.isalpha():
        w.append(se)
    elif se.isdigit():
        n.append(se)
    else:
        pass

#alphanumeric
if len(w)>0 or len(n)>0:
    print(True)
else:
    print(False)

#alpha
if len(w)>0:
    print(True)
else:
    print(False)

#digit
if len(n)>0:
    print(True)
else:
    print(False)

#lower
i=0
while i < len(w):
    if w[i].islower():
        print(True)
        break
    i += 1
else:
    print(False)

#upper
j=0
while j < len(w):
    if w[j].isupper():
        print(True)
        break
    j += 1
else:
    print(False)

