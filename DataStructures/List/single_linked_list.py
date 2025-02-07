def new_list ():
    newlist = {
        "first": None,
        "last": None,
        "size": 0,
    }
    
    return newlist

def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    return node["info"]

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1
            
    if not is_in_array:
        count = -1
    return count

def new_list ():
    new_list = {
        "first" : None,
        "last" : None,
        "size" : 0,
    }
    return new_list
        
        
def new_single_node(element):
    
    return {"info": element, "next": None}


def add_first(my_list, element):
    nodo = new_single_node(element)
    
    nodo["next"] = my_list["first"]
    my_list["first"] = nodo
    
    if my_list["size"] == 0:
        my_list["last"] = my_list["first"]
        
    my_list["size"] += 1
    
    return my_list

def size(my_list):
    size = my_list["size"]
    return size
    

    
    
    