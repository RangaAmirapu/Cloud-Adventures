if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, (input().split(" "))))
    arr.sort()
    
    def RemoveDup(inputList) :
        secondList  =[]
        for element in inputList:
            if element not in secondList:
                secondList.append(element)
        return secondList
    
    arr = RemoveDup(arr)
    print((arr[len(arr)-2]))