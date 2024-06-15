import parser_library

# Tokenization is needed to easily select tokens and group, target them against other tokens.
# Associate p start tag with p end tag. 

def htmltotokens(htmlstring, token = "", starttokenization = False, closingtag = False):
    for letter in htmlstring:
        if letter == '<': starttokenization = True; continue

        if letter == '>': print(token, closingtag); starttokenization = False;  token = ""; 
            
        if starttokenization: token += letter
        if starttokenization and letter == "/": closingtag = True





       
           
           


htmltotokens(parser_library.htmltostring("example.html"))
print()
print("Tokenization")