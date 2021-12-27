# Rough Work

# Input : int[] InputArray, int target
# Output : int[] indices #Indices of items that sum to target

# Assumption :- Exactly One Solution #Return the first answer(indice value) that matches the sum of target 

# To Note :- Do Not repeat The same index

# Solution 1 : 
# BruteForceWay

#TimeComplexity : O(n)

def TwoSum(target : int , input_array = [int] ) -> int :
    for i in range(0,len(input_array)):
        current_ele = input_array[i]
        for j in range (0,len(input_array)):
            #print("------")
            if input_array[j] == current_ele:
                pass
            elif current_ele + input_array[j]  == target:
                #print(str(current_ele) +" + "+ str(input_array[j]))
                return [i,j]
        
    return 0

print(TwoSum(5,[3,2,6]))

