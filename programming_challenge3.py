## Programming Challenge 3.a
def is_in_range(num):
    '''Function to check if given number is within range 4 to 10 inclusive.
    :param num
        **MANDATORY** Number
    :return: Boolean value'''
    
    return num in range(4,11)

## Programming Challenge 3.b
def is_list_empty(input_list):
    '''Function to check if input_list is empty.
    :param input_list
        **MANDATORY** list
    :return
        "EMPTY" if list is empty else "NOT EMPTY"'''
    
    if isinstance(input_list, list):
        if input_list:
            return 'NOT EMPTY'
        else:
            return 'EMPTY'
            
## Programming Challenge 3.c
def write_to_file(filename, data):
    '''Function to write data to a file with the given filename
    :param filename
        **MANDATORY** Name of the file
    :param data
        **MANDATORY** Data string to be written to file
    :return: None'''
    
    try:
        # Writing to file in append mode
        with open(filename, 'a+') as fh:
            fh.write(data)
    except PermissionError as e:
        print("ERROR: Write permission issues, please check.\n" + str(e))
        
## Programming Challenge 3.d
def double(input_list=[]):
    '''Function to double each value in a list.
    :param input_list
        **OPTIONAL** List. Default value is empty list
    :return: New list with each value of input_list doubled'''
    
    # Double each value using list comprehension and return
    return [x*2 for x in input_list]
