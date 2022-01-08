from collections import deque

def search(name,graph):
    search_queue = deque() #Creates A new Queue
    search_queue += graph[name] #Adding 1st Node Connections to queue
    searched = [] #Adding Visited Notes to Searched to avoid revisiting nodes
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person +" is mango seller")
                return True
            else:
                searched.append(person)  # Append to Searched
                if person in graph:   #checking if node has more connections
                    search_queue += graph[person]
                
                #print(person)
    print("No Mango Seller Found")           
    return False

def person_is_seller(name):
    return name[-1] == 'm'


graph_1 = {}
graph_1["you"] = ["simran", "parmeet", "harmeet"]
graph_1["parmeet"] = ["gurneet", "zombie"]
graph_1["harmeet"] = ["Sneha", "Utkarsh"]


graph_2 = {}
graph_2["you"] = ["simran", "parmeet", "harmeet"]
graph_2["parmeet"] = ["gurneet", "zombie"]
graph_2["harmeet"] = ["Sneha m", "Utkarsh"]

print("Test Case 1 : Graph 1 with no Mango Seller:")
search("you",graph_1)
print("Test Case 2 : Graph 2 with a Mango Seller:")
search("you",graph_2)