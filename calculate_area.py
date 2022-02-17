# by Kami Bigdely
# Rename Method
# Reference: https://parade.com/1039985/marynliles/pick-up-lines/

def calc_area(graph):  
    """Calculate the area under the input graph."""
    # bla bla bla.
    pass

#####################

def get_max(li): 
    max_num = li[0]
    for value in li:
        if value > max_num:
            max_num = value
    return max_num


li = [5, -1, 43, 32, 87, -100]
print(get_max(li))

############################
def create_word_list(sentence):  # TODO: Rename this function to reflect what it's doing.
    words = sentence[0:].split(' ')
    return words

print(create_word_list()('If you were a vegetable, you’d be a ‘cute-cumber.'))
