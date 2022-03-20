if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
a=list(arr)
b=[]
def runnerup():
    for i in range(len(a)):
        if a[i]!=max(a):
            b.append(a[i])
runnerup()
print(max(b))