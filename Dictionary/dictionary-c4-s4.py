#1
word = input()
dic = {}
for key in range(len(word)):
    if word[key] != " ":
        if word[key] not in dic:
            dic[word[key]] = 1
        else:
            dic[word[key]] += 1
print(dic)

#2
payment = eval(input())
total = 0
for key in payment:
    total += key["price"]*key["quantity"]
print(total)

# # or 
# payment = eval(input())
# total = 0
# for key in payment:
#     for value in key:
#         if value == "price":
#             total += key["price"]*key["quantity"]
# print(total)

# 3
nameOfIng = input()
quantityOfIng = int(input())
listOfIngAQuan = eval(input())
enough = False
for value in listOfIngAQuan:
    if value["ingredient"] == nameOfIng:
        if value["quantity"] - quantityOfIng >= 0:
            enough = True
            value["quantity"] = value["quantity"] - quantityOfIng
if enough:
    print(listOfIngAQuan)
else:
    print("There is not enough stock in the kitchen for this ingredient")


# or mind 
name = input()
quantity = int(input())
listOfIn = eval(input())
limited = True
message = "There is not enough stock in the kitchen for this ingredient"
for key in listOfIn:
    if key["ingredient"] == name:
        if key["quantity"] >= quantity:
            key["quantity"] -= quantity
        else:
            limited = False
if limited:
    print(listOfIn)
else:
    print(message)