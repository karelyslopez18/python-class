name_list=['Joe','Ned','Joe','Bob','Jim','Joe', 'Jim']

def remove_duplicates(name_list):
    name_list2=[]
    for y in range(len(name_list)):
        x = 0
        for z in range(len(name_list2)):
            if name_list[y] == name_list2[z]:
                x = 1
        if x == 0:
            name_list2.append(name_list[y])
    return name_list2
