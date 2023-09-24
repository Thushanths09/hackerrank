def count_substring(string, sub_string):
    subStrings = []
    for i in range(len(string)):
        subStrings.append(string[i:(len(sub_string)+i)])
    count = 0
    for j in range(len(subStrings)):
        if sub_string == subStrings[j]:
            count += 1
    return count



if __name__ == '__main__':
    string = input("Enter a word")
    sub_string = input("Enter a sub word")
    count = count_substring(string, sub_string)
    print(count)
