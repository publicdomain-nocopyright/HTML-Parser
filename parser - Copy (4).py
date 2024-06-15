import parser_library

# Tokenization is needed to easily select tokens and group, target them against other tokens.
# Associate p start tag with p end tag. 


def begintokenization():
    global tokenization
    tokenization = True

def stoptokenization():
    global tokenization
    tokenization = False

def htmltotokens(htmlstring, token = "", closingtag = False):
    for letter in htmlstring:
        if letter == '<': begintokenization(); continue
        if letter == '>':  stoptokenization(); print(token, closingtag); token = ""; 
            
        if tokenization: token += letter
        if tokenization and letter == "/": closingtag = True




       
           
           


htmltotokens(parser_library.htmltostring("example.html"))
print()
print("Tokenization")