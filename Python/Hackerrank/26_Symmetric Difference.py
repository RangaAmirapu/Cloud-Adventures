n1 = int(input())
arr1 = list(map(int, input().split()))
n2 = int(input())
arr2 = list(map(int, input().split()))

set1 = set(arr1)
set2 = set(arr2)
resSet = (sorted(set1.symmetric_difference(set2)))
for s in resSet:
    print(s)
