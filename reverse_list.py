list_to_reverse = [10,20,30,40,50,60]

#--------------------------------------------------
#Approach_1
#iterative method with extra list 
#complexity O(n)
def Reverse_Approach1(list_to_reverse):
    revered_list = []
    for i in range(len(list_to_reverse)-1,-1,-1):
        revered_list.append(list_to_reverse[i])
    return revered_list

#reversed_list = Reverse_Approach1(list_to_reverse)
#print(reversed_list)

#--------------------------------------------------
#Approach_2
#Pythonic Way
def Reverse_Approach2(list_to_reverse):
    return list_to_reverse[::-1]
#reversed_list = Reverse_Approach1(list_to_reverse)
#print(reversed_list)

#--------------------------------------------------
#Approach_3
#reursive method without extra list   



    
    
    
