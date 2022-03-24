if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

def avg_list(li):
    average=sum(li)/len(li)
    avg_format="{:.2f}".format(average)
    print(avg_format)
x= student_marks[str(query_name)]
avg_list(x)
