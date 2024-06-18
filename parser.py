import parser_library

# Tokenization is needed to easily select tokens and group, target them against other tokens.
# Associate p start tag with p end tag. 



def htmltotokens(htmlstring):
    tokens = []
    token = ""

    default_attributes = {"is_closing_tag": False, "waffles": 5} 

    is_tokenizing = False

    for letter in htmlstring:
        if letter == '<': is_tokenizing = True; attributes = default_attributes.copy(); continue      
        if letter == '>': is_tokenizing = False; tokens.append((token, attributes)); token = ""; continue;

        if is_tokenizing:
            if letter == '/':
                attributes["is_closing_tag"] = True
            token += letter

    return tokens

tokens = htmltotokens(parser_library.htmltostring("example.html"))

for token in tokens:
    print(token)