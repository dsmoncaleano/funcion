def sumlist(myList) :
     
    result = 0
    for x in myList:
         result = result + x
    return result
     
list1 = [8, 2, 3, 0, 7]
print(sumlist(list1))