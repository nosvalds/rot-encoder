# ROT-13 function
# n - rotation value (1 - 25)
# string - string to be encoded
def ROT(n, string):
    # input validation
    if (not string):
        return "Please enter a string to encode"
    if (not isinstance(n, int)):
        return "Rotation must be an integer"
    if (n < 1 or n > 25):
        return "Rotation must be 1 - 25"
    
    # create dictionary using offset n
    code = dict()
    from string import ascii_lowercase
    from string import ascii_uppercase
    for i, letter in enumerate(ascii_lowercase):
        code[letter] = ascii_lowercase[(i + n) % 26]
    for i, letter in enumerate(ascii_uppercase):
        code[letter] = ascii_uppercase[(i + n) % 26]
    
    # iterate over our string and replace
    result = ""
    for char in string:
        if char in code: # only replace if it's in the dictionary
            result += code[char]
        else:
            result += char
    
    return result

def runTests():
    # validation tests
    print(ROT(1.5, "Hello")) # "Rotation must be an integer"
    print(ROT(27, "Hello")) # "Rotation must be 1 - 25"

    # Final Tests
    print(ROT(13, "Hello World")) # "Uryyb Jbeyq"
    print(ROT(13, "The Number 16.")) # "Gur Ahzore 16."
    print(ROT(19, "Hello World!")) # "Axeeh Phkew!"

runTests()
