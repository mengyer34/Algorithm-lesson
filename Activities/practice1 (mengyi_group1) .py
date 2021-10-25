
# #1
# def remove(word):
#     newName = ""
#     isFound = True
#     for i in range(len(word)):
#         if word[i]!="-":
#             newName += word[i]
#     return newName
# Choice = True
# while Choice:
#     text = input()
#     a = remove(text)
#     print(a)
#     ask = input("Do you want to continous (Y/N)?: ")
#     if ask != "Y":
#         Choice = False

# #2
# def sumNum(number1, number2):
#     return number1 + number2
# n1 = int(input())
# n2 = int(input())
# a = sumNum(n1, n2)
# print(a)


# #3
# def sum(n1, n2):
#     sumAll = n1 + n2
#     return sumAll
# numberOfVar = int(input("Number of Value : "))
# allNum = 0
# for i in range (numberOfVar):
#     value = int(input("Value "+str(i+1)+" : "))
#     allNum = sum(allNum, value)
# print("The sum is : ", allNum)

# #4
# def sumFrom(x, y):
#     result = 0
#     for i in range(x, y+1):
#         result += i
#     return result
# start = int(input("start value: "))
# end = int(input("End value: "))
# a = sumFrom(start,end)



# #4
# def sum(numStart, numEnd):
#     result = 0
#     for i in range(numStart, numEnd + 1):
#         result += i
#     return result
# start = int(input("start value: "))
# end = int(input("End value: "))
# sumNum = sum(start, end)
# print(sumNum)


# #5
# def numberOfUpperCases(word):
#     result = 0
#     for i in range(len(word)):
#         if word[i]==word[i].upper():
#             result += 1
#     return result
# a = input()
# print(numberOfUpperCases(a))



# # start counter
# def count(a, b):
#     result = 0
#     for i in range(a, b+1):
#         result += i
#     return result
# n1 = int(input())
# n2 = int(input())
# print(count(n1,n2))

# # count_uppercase
# def count_uppercase(word):
#     result = 0
#     for i in range(len(word)):
#         if word[i].isupper():
#             result += 1
#     return result
# text = input()
# print(count_uppercase(text))

# #2
# def countGreater(arr):
#     result = 0
#     for i in range(1,len(arr)):
#         if arr[i-1]<arr[i]:
#             result += 1
#     return result
# print(countGreater(eval(input())))

#3
def countA(arr):
    result = 0
    for word in arr:
        for i in len(word):
            if word[i]=="a" or word[i]=="A":
                result +=1
    return result
a = ['book','apple']
print(countA(a))
    

    

    


    










