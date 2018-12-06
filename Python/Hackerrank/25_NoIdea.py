n,m = map(int, input().split())
arrAsSet = (list(map(int, input().split()))) 
setA = set((map(int, input().split()))) 
setB = set((map(int, input().split()))) 

happiness = 0

for i in arrAsSet:
    if i in setA:
        happiness += 1

for i in arrAsSet:
    if i in setB:
        happiness -= 1
    
print(happiness)

