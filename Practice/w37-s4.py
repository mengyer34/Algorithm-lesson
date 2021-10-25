# # 1
# def numberOfEight(array):
#     result = 0
#     for i in array:
#         if i==8:
#             result += 1
#     return result
#     # Enter your code here:
# array = eval(input())    
# print(numberOfEight(array))

# # 2
# array = eval(input())
# word = input()
# numberOfIndex = int(input())
# array.insert(numberOfIndex, word)
# print(array)


# # 3
# def splitBySpace(text):
#     newWord = ''
#     array = []
#     for i in text:
#         if i == " ":
#             array.append(newWord)
#             newWord = ''
#         else:
#             newWord += i
#     if newWord:
#         array.append(newWord)
#     return array
# text = input()
# print(splitBySpace(text))

# # 4
# def reverseArray(array):
#     newArray = []
#     for i in range(-1, -(len(array)+1), -1):
#         if array[i]%2 == 1:
#             newArray.append(array[i])
#     return newArray
# print(reverseArray(eval(input())))



# 5
def maxNumber(list):
    max = 0
    for i in list:
        if i > max:
            max = i
    return max

def replaceNum(arr):
    newArr = [] 
    for i in arr:     
        if i < 5:
            newArr.append(maxNumber(arr))
        else:
            newArr.append(i)
    return newArr
array = eval(input())
print(replaceNum(array))




