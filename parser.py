def htmltostring(textfile):
    textstring = "" 
    with open(textfile) as file:
        for line in file.read():
            for letter in line:
                if letter == '\n':
                    continue
                textstring += letter
    return textstring

def htmltotokens(htmlstring):
    token = ""
    for letter in htmlstring:
        token += letter
        print(token)
        if token == "<html>":
            print(token)
            token = ""

        print(letter, end="")


htmltotokens(htmltostring("example.html"))
print()
print("Tokenizationm")