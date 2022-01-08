#2. Sort an array of 0’s 1’s 2’s without using extra space or sorting algo 


input_list = [0,2,0,1,0,1,2,0,1,0,0]

def Solution_1(input_list):
    low = 0
    high = len(input_list)-1
    mid = 0     #int(( start + end )/2)
    
    while mid<= high:
        if input_list[mid] == 0:
            input_list[low],input_list[mid] = input_list[mid],input_list[low]
            #print(current)
            low = low + 1
            mid = mid+1
        elif input_list[mid] == 1:
            mid = mid +1
        else:
            input_list[mid],input_list[high] = input_list[high],input_list[mid]
            high = high - 1
        #else:
           # print(current," skipped")
        
    return input_list
    
Sorted_Arr = Solution_1(input_list=input_list)
print(Sorted_Arr)


#print(len(input_list))