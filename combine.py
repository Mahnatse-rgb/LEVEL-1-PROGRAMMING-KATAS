def combine(list1, list2):
    lst = []
    len1 = len(list1)
    len2 = len(list2)
    
  

    for index in range( max(len1, len2) ):
        if index+1 <= len1:
            lst += [list1[index]]

        if index+1 <= len2:
            lst += [list2[index]]
            
        

    return lst
    
myList1 = [11,22,33]
myList2 = [1,2,3]

lst = combine(myList1, myList2)

print(lst)