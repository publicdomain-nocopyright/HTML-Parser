import parser_library

# Tokenization is needed to easily select tokens and group, target them against other tokens.
# Associate p start tag with p end tag. 

def htmltotokens(htmlstring, token = "", begintokenization = False, closingtag = False):
    for letter in htmlstring:
        if letter == '<': begintokenization = True; continue
        if letter == '>': print(token, closingtag); begintokenization = False;  token = ""; 
            
        if begintokenization: token += letter
        if begintokenization and letter == "/": closingtag = True

htmltotokens(parser_library.htmltostring("example.html"))

print()
print("Tokenization")