N=int(input("Enter Student Numbers: "))
b=[]
if __name__ == '__main__':
    for i in range(N):
        name = input("enter your name: ")
        score = float(input("Enter Score: "))
        a=[name,score]
        b.append(a)
c=[]
for j in b:
    c.append(j[1])
print(b[c.index(min(c))][0])

    


        
