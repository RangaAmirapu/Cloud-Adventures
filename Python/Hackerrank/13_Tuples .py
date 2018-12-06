if __name__ == '__main__':
    n = int(input())
    integer_list = input().strip().split(" ")
    array  = []
    for i in range(0, n):
       array.append(int(integer_list[i]))
    
    tu = tuple(array)
    print (hash(tu))
