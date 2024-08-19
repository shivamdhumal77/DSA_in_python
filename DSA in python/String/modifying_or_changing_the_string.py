''' Modifying character in String
To modify any Character in a String, we need:

A character that is to replaced in the string (say “ch”)
A position/index of the Character where it is to be replaced at. (say “k”)
Below is the implementation of the above approach:'''

def replace_character_at_index(string,index,new_character):
    string_list = list(string)
    # converting to list to allow modification
    string_list[index] = new_character
    
    # convert back to string and return
    return ''.join(string_list)

def main():
    # Original string
    original_string = "Geeks Gor Geeks"

    # Index to replace character
    index = 6

    # New character
    new_character = 'F'

    # Print original string
    print("Original String =", original_string)

    # Replace character at the specified index
    modified_string = replace_character_at_index(
        original_string, index, new_character)

    # Print modified string
    print("Modified String =", modified_string)


# Entry point of the program
if __name__ == "__main__":
    main()