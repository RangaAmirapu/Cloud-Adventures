if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    average  = (student_marks[query_name][0] + student_marks[query_name][1] + student_marks[query_name][2])/3
    average=format(average, '.2f')
    print (average)