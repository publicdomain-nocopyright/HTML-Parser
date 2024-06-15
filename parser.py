import parser_library

# Tokenization is needed to easily select tokens and group, target them against other tokens.
# Associate p start tag with p end tag. 
def htmltotokens(htmlstring, token = "", starttokenization = False, closingtag = False):
    for letter in htmlstring:
        if starttokenization:
            if letter != '>':
                token += letter
                if letter == "/":
                    closingtag = True

        if starttokenization == False:
            if token != "": 
                print(token)

        if letter == '<': starttokenization = True
        if letter == '>': starttokenization = False

        if letter == '>':
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


htmltotokens(parser_library.htmltostring("example.html"))
print()
print("Tokenization")