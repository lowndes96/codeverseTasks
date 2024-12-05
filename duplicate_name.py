def name_sorter(text_file):

    output_dict = {
    'non-duplicates' : [], 
    'duplicates': []
    }
    #take list from file and asign to non-duplicate list within output_dict 
    with open(text_file, 'r') as name_list:
        for line in name_list: 
            name1 = line.rstrip('\n')
            output_dict['non-duplicates'].append(name1)

    for index1, name1 in enumerate(output_dict['non-duplicates']): 
            for name2 in output_dict['non-duplicates'][index1+1:]: 
                if (name1 == name2): 
                    output_dict['duplicates'].append(name1) #duplicates added to dict list
                    output_dict['non-duplicates'].pop(index1) # pop higher indexed name 
                    output_dict['non-duplicates'].remove(name1) #remove lower indexed name 

    print(f'non-duplicates: \n {output_dict["non-duplicates"]} \n duplicates: \n {output_dict["duplicates"]}')

                    

name_sorter('name_input.txt')

