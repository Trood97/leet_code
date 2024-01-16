
def balance_the_universe(string:str)-> int:
    stack = []                 #to keep track of the open
    additional_elements = 0    #if open bracket runs out
    for char in string:
        if char == '(':
            stack.append(char)      #as simple as that
        elif char == ")":
            if stack:               #cancelling out, (balancing)
                stack.pop()
            else:
                additional_elements+=1     #creating a balance

    return additional_elements + len(stack)       #the left elements and added ones





