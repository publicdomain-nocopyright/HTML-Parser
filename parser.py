import parser_library

# Tokenization is needed to easily select tokens and group, target them against other tokens.
# Associate p start tag with p end tag. 
# TODO: Tags nesting support and text association with tags.



def htmltotokens(htmlstring):
    tokens = []
    token = ""

    default_attributes = {"is_closing_tag": False, "waffles": 5} 

    is_tokenizing = False

    # Tag Scanning, processing, tokenization
    for letter in htmlstring:
        if letter == '<': is_tokenizing = True     
        if letter == '<': attributes = default_attributes.copy();
        if letter == '<': continue
        
        if letter == '>': is_tokenizing = False
        if letter == '>': tokens.append((token, attributes)); 
        if letter == '>': token = ""
        if letter == '>': continue

        if is_tokenizing:
            if letter == '/':
                attributes["is_closing_tag"] = True
            token += letter
        else:
            print(letter)

    return tokens

tokens = htmltotokens(parser_library.htmltostring("example.html"))

print("____________")
for token in tokens:
    for letter in token[0]:
        if letter == ' ':
            break
        print(letter, end="")