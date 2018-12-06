def swap_case(s):
    
    charList  = list(s)
    ListLen =  len(charList)
    for c  in range(ListLen):
        if (charList[c].isupper()):
            charList[c] = charList[c].lower()
            
        elif (charList[c].islower()):
            charList[c] = charList[c].upper()

    return ''.join(charList)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)