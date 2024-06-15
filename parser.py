def htmltostring(textfile):
    textstring = "" 
    with open(textfile) as file:
        for line in file.read():
            for letter in line:
                if letter == '\n':
                    continue
                textstring += letter
    return textstring


# Tokenization is needed to easily select tokens and group, target them against other tokens.
def htmltotokens(htmlstring, token = "", starttokenisation = False):
    for letter in htmlstring:
        
        if starttokenisation:
            token += letter
        if starttokenisation == False:
            if token != "": 
                print(token)

        if letter == '<':
            starttokenisation = True
        if letter == '>':
            starttokenisation = False
            print(token)
            token = ""

        #if token == "<html>":
        #    print(token)
        #    token = ""
#
        #print(letter, end="")


htmltotokens(htmltostring("example.html"))
print()
print("Tokenizationm")