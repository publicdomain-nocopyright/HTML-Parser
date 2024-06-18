import parser_library

# Tokenization is needed to easily select tokens and group, target them against other tokens.
# Associate p start tag with p end tag. 



def htmltotokens(htmlstring):
    tokens = []
    token = ""
    init_attributes = {"is_closing_tag": False, "waffles": 5} 
    attributes = init_attributes.copy() 

    is_tokenizing = False

    for letter in htmlstring:
        if letter == '<': is_tokenizing = True; attributes.update(init_attributes); continue      
        if letter == '>': is_tokenizing = False; tokens.append((token, attributes["is_closing_tag"])); token = ""; continue;

        if is_tokenizing:
            if letter == '/':
                attributes["is_closing_tag"] = True
            token += letter

    return tokens

tokens = htmltotokens(parser_library.htmltostring("example.html"))

for token in tokens:
    print(token)