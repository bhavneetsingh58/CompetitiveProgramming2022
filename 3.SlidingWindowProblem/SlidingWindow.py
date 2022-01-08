def sliding_window(input)-> int:
    max_list = []
    if input == []:
        return False
    if len(input) == 1:
        return input[0]
    for i in range(0,len(input)-2):
        max_list.append(max(input[i],input[i+1],input[i+2]))
    return max(max_list)


print("---------------------------------------")
print("Test Case : Empty List")
input_list = []
print(sliding_window(input_list))
print("---------------------------------------")
print("Test Case : One Element in List")
input_list = [5]
print(sliding_window(input_list))
print("---------------------------------------")
print("Test Case : n Element in List")
input_list = [5, 6, 1, 2, 3, 0, 8, 7]
print(sliding_window(input_list))
