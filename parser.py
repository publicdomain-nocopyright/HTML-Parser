import parser_library

# Tokenization is needed to easily select tokens and group, target them against other tokens.
# Associate p start tag with p end tag. 
# TODO: Tags nesting support and text association with tags.



def htmltotokens(htmlstring : str):
    token  : str = str("")
    tokens : list[str] = []

    default_attributes : dict = {"is_closing_tag": False, "waffles": 5} 

    is_tokenizing : bool = False

    # Tag Scanning, processing, tokenization
    for letter in htmlstring:
        if letter == '<': 
            is_tokenizing = True; 
            token = str("")
            attributes = default_attributes.copy();
            continue
        
        if letter == '>': 
            if token is not None: 
                tokens.append((token, attributes)); 
                token = str("")
                is_tokenizing = False
                continue

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
    if token[0] is None:
        print("stopped here" + str(token))
        input()
    for letter in token[0]:
        if letter == ' ':
            break
        print(letter, end="")