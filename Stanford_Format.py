# This function takes in a list of tuples from Stanford's tagging as its parameter
# and turn it into our standard format. The output of the function is a string:
# Qiaotong\tabPER
# Wu\tabPER



def stanford_format(list_of_taggings):
    out_str = '\n'   
    length = len(list_of_taggings)
    for i in range(length):
        tag_tuple = list_of_taggings[i]
        if tag_tuple[1] == 'PERSON':
            out_str = out_str + tag_tuple[0] + '\tPER\n'
        elif tag_tuple[1] == 'ORGANIZATION':
            out_str = out_str + tag_tuple[0] + '\tORG\n'
        elif tag_tuple[1] == 'LOCATION':
            out_str = out_str + tag_tuple[0] + '\tLOC\n'
        else:
            out_str = out_str + tag_tuple[0] + '\tO\n'
    out_str = out_str + '\n'
    return out_str




