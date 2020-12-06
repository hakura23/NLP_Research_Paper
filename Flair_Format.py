# The method's parameter is a list of taggings from Flair, and the method returns a formatted string
# Since the label of Flair is of the form "B-LOC", the methods use string[2:] to truncate the "B-" part
def flair_format(list_of_taggings):
    out_str = '\n'   
    length = len(list_of_taggings)
    for i in range(length):
        tag_tuple = list_of_taggings[i]
        if tag_tuple[1][2:]== 'PER':
            out_str = out_str + tag_tuple[0] + '\tPER\n'
        elif tag_tuple[1][2:] == 'ORG':
            out_str = out_str + tag_tuple[0] + '\tORG\n'
        elif tag_tuple[1][2:] == 'LOC':
            out_str = out_str + tag_tuple[0] + '\tLOC\n'
        else:
            out_str = out_str + tag_tuple[0] + '\tO\n'
    out_str = out_str + '\n'
    return out_str
