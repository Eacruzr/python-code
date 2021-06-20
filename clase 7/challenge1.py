def capital_indexes(linea):
    word = list(linea)
    index_list = []
    i = 0
    while i < len(word):
        if word[i].upper() == word[i]:
            index_list.append(i)
        i+=1
    return(index_list)
        
print(capital_indexes("HeLlO"))