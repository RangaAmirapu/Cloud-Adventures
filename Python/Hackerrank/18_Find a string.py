def count_substring(string, sub_string):
    lengthOfString = len(string)
    lengthOfSubString  = len(sub_string)
    count = 0
    for i in range(0, lengthOfString):
        tmp = string[i:i+lengthOfSubString]
        if(tmp == sub_string):
            count = count + 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)