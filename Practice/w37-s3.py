# # # 1
# def RemoveDuplicate(word):
#     result = []
#     for i in word:
#         for j in range(1, len(i)):      
#             if i[j-1] != i[j]:
#                 result.append(i[j-1])
#     result += j[-1]
#     return result
# word = eval(input())
# sorted_word = sorted(word)
# print(RemoveDuplicate(sorted_word))

# def RemoveDuplicate(word):
#     result = []
#     for i in range(1, len(word)):
#         if word[i-1] != word[i]:
#             result.append(word[i-1])
#     result += word[-1]
#     return result
# word = input()
# sorted_word = sorted(word)
# print(RemoveDuplicate(sorted_word))


# def RemoveDuplicate(word1):
#     result = []
#     for word in word1: 
#         for i in range(1, len(word),1):
#             if word[i-1] != word[i]:
#                 result.append(word[i-1])
#     # result += word[-1]
#     result.sort()
#     return result
# word = ['banana']
# print(RemoveDuplicate(word))

# for i in lseparatedOrbList:
#        for j in lseparatedOrblist:
#         if lseparatedOrbList[i] == lseparatedOrbList[j]:
#             lseparatedOrbList.remove(lseparatedOrbList[j])


# def remove_duplicates(word):
#     t = word
#     t2 = word
#     for t in t2:
#         t.append(t2.pop(t))
#     return t
# print(remove_duplicates(input()))



# # 3
# def findIndexOfSeven(array):
#     #write your code here: 
#     for i in len(array):
#         if array(i)!=7:
#             array.append(i)
#     return array

# array = eval(input())
# print(findIndexOfSeven(array))
# #write your code here.



# # 4
# array = eval(input())
# for i in range(len(array)):
#     for j in range(len(array[i])):
#         value = array[i][j]
#         if value == 7:
#             array[i][j] = 8
# print(array)


# # 2
# def getMinimumIndex(list):
#     temp = 1
#     orderedList = []
#     for i in list:
#         if i < temp:
#             orderedList.append(i)
#         temp += 1
#     return orderedList

# def sumAllelement(arr):
#     result = 0
#     for i in arr:
#         result += i
#     return result 

# print(getMinimumIndex(eval(input())))
# # print(sumAllelement(eval(input())))

# # 2
# def getMinimumIndex(list):
#     minIndex=0
#     for  i in range(len(list)):
#         if i>0 and list[i] < list[i-1]:
#             minIndex=i
#     return minIndex
# def removeMinimun(array):
#     orderedList=[]
#     for i in range(len(array)):
#         orderedList.append(array[getMinimumIndex(array)])
#         array.pop(getMinimumIndex(array))
#     return orderedList
# array=eval(input())
# print(removeMinimun(array))

# oldList = eval(input())
# newList = []
# index = 0
# def getMiniIndex(numbers):
#     miniNum = numbers[0]
#     index = 0
#     for i in range(1, len(numbers)):
#         if miniNum > numbers[i]:
#             miniNum = numbers[i]
#             index = i
#     return index

# while oldList:
#     index = getMiniIndex(oldList)
#     newList.append(oldList[index])
#     oldList.pop(index)
    
# print(newList)
    
# # 2
# array = eval(input())
# for i in range(len(array)):
#     for j in range(i + 1, len(array)):
#         if array[i] > array[j]:
#             array[i], array[j] = array[j], array[i]
# print(array)

# oldArray = eval(input())
# def getMiniIndex(numbers):
#     minNumber = numbers[0]
#     indexOfNum = 0
#     for index in range(1, len(numbers)):
#         if minNumber > numbers[index]:
#             minNumber = numbers[index]
#             indexOfNum = index
#     return indexOfNum


# newArray = []
# while oldArray:
#     minIndex = getMiniIndex(oldArray)
#     newArray.append(oldArray[getMiniIndex(oldArray)])
#     oldArray.pop(minIndex)
# print(newArray)