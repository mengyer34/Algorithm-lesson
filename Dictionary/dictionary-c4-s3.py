# # 1
# dictionary = eval(input())
# result = "No teacher here!"
# allOfEle = 0
# value = 0
# if len(dictionary)>0:
#     result = 0
#     for i in dictionary:
#         value += dictionary[i]
#         allOfEle += 1
#     result = value/allOfEle
# print(result)

# # 2
# # Enter your code here. Read input from STDIN. Print output to STDOUT
# dictionary = eval(input())
# fruit = 0
# meat = 0
# for key in dictionary:
#     for key2 in key:
#         if key2 == "fruit":
#             fruit += 1
#         elif key2 == "meat":
#             meat += 1
# print("Fruit:"+str(fruit)+"\n"+"Meat:"+str(meat))
        
# 3

def getMax(arr):
    result = arr[0]
    for i in arr:
        if i > result:
            result = i
    return result

def getMin(arr):
    result = arr[0]
    for i in arr:
        if result > i:
            result=i
    return result
# # or 
# def getMin(arr):
#     minumum = arr[0]
#     for i in arr:
#         if i < minumum:
#             minumum = i
#     return minumum

def getAvg(arr):
    result = getMax(arr) + getMin(arr)
    return result//2
 

list = eval(input())   
result = {}
result["max"] = getMax(list)
result["min"] = getMin(list)
result["avg"] = getAvg(list)
print(result)

#4
studentsData = eval(input())
score = 0
lessThan75 = 0
for i in studentsData:
    for key in i:
        if i["name"] and i["score"] > score:
            score = i["score"]
        if i["score"] < 75:
            lessThan75 += 1
if score == 0:
    print("No result")
else:
    print("The best student is "+ i["name"])  
if lessThan75 == 0 and score > 0:
    print("All students have more than 75")