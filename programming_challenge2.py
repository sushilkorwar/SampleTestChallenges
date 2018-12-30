## Programming challenge 2
def get_unique_chars(s1, s2):
    '''Function to check and return string of unique characters.
    :param s1
        **MANDATORY** First string input
    :param s2
        **MANDATORY** Second string input
    :return: String of unique characters'''
    
    # Convert string to set
    t1 = set([s for s in s1.lower()])
    t2 = set([s for s in s2.lower()])
    
    # Convert union set as string using join and return new string
    return ''.join(t1.union(t2))
