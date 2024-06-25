def htmltostring(textfile):
    textstring = "" 
    with open(textfile) as file:
        for line in file.read():
            for letter in line:
                if letter == '\n':
                    continue
                textstring += letter
    return textstring


# self-executing function for function decorator
# @execute
def execute(func):
    func()
    return func
    
def Empty(string):
    return string == ""

# if Empty(my_string):