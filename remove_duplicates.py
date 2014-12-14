#remove_duplicate integers 
def remove_duplicates(given_list):
    no_dups = {}
    no_dups_list = []
    
    for item in given_list:
        if item not in no_dups:
            no_dups[item] = item
        
    for item in no_dups:
        no_dups_list.append(item)
    
    return no_dups_list