def max_ones(list_to_search):
    count = 0
    max = 0
    for i in list_to_search:
        if i == 1:
            count = count + 1
            if max < count :
                max = count
        else:
            count = 0
    return max
            
            
            
        
        
list_to_search = [0,0,1,1,1,0,0,1,1,0,1,1,1,1,0]
print(max_ones(list_to_search=list_to_search))
        