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
# Associate p start tag with p end tag. 
def htmltotokens(htmlstring, token = "", starttokenisation = False, closingtag = False):
    for letter in htmlstring:
        
        if starttokenisation:
            if letter != '>':
                token += letter
                if letter == "/":
                    closingtag = True

        if starttokenisation == False:
            if token != "": 
                print(token)

        if letter == '<':
            starttokenisation = True
        if letter == '>':
            starttokenisation = False
            print(token)
            if closingtag:
                print("It's a closing tag!")
            token = ""
            closingtag = False

        #if token == "<html>":
        #    print(token)
        #    token = ""
#
        #print(letter, end="")


htmltotokens(htmltostring("example.html"))
print()
print("Tokenizationm")