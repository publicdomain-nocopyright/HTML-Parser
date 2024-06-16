import parser_library

# Tokenization is needed to easily select tokens and group, target them against other tokens.
# Associate p start tag with p end tag. 

def htmltotokens(htmlstring):
    tokens = []
    token = ""
    is_tokenizing = False
    is_closing_tag = False

    for letter in htmlstring:
        if letter == '<': is_tokenizing = True; is_closing_tag = False; continue      
        if letter == '>': is_tokenizing = False; tokens.append((token, is_closing_tag)); token = ""; continue;

        if is_tokenizing:
            if letter == '/':
                is_closing_tag = True
            token += letter

    return tokens

tokens = htmltotokens(parser_library.htmltostring("example.html"))

for token in tokens:
    print(token)