import parser_library

# Tokenization is needed to easily select tokens and group, target them against other tokens.
# Associate p start tag with p end tag. 
# TODO: Tags nesting support and text association with tags.



def htmltotokens(htmlstring : str):
    token  : str = str("")
    tokens : list[str] = []
    letter : str = str('')

    default_attributes : dict[str, any] = {"is_closing_tag": False, "waffles": 5} 
    attributes : dict[str, any] = default_attributes.copy()

    is_tokenizing : bool = False

    # Tag Scanning, processing, tokenization
    for letter in htmlstring:
        if letter == '<': 
            token = None
            attributes = default_attributes.copy();
            is_tokenizing = True; 
            continue
        

        if is_tokenizing:
            if token is None: 
                token = "" 
            if token is not None and not letter == '>':
                token += letter
                if letter == '/':
                    attributes["is_closing_tag"] = True
            
        else:
            print(letter)

        if letter == '>': 
            if token is not None: 
                tokens.append((token, attributes)); 
                is_tokenizing = False
                del token
                continue
    return tokens

tokens = htmltotokens(parser_library.htmltostring("example.html"))

print("____________")
print(tokens)
for token in tokens:
    if token[0] is None:
        print("stopped here" + str(token))
        input()
    for letter in token[0]:
        if letter == ' ':
            break
        print(letter, end="")