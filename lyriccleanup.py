

#Wack string in Good string out
def process_string(input_string):
    # Remove all occurrences of a standalone backslash
    input_string = re.sub(r'\\(?![n])', '', input_string)
    
    # Replace all occurrences of \n with a single space
    input_string = re.sub(r'\\n', ' ', input_string)
    
    return input_string
