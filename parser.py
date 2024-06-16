import parser_library

# Tokenization is needed to easily select tokens and group, target them against other tokens.
# Associate p start tag with p end tag. 



def htmltotokens(htmlstring):
    attributes =  {"is_closing_tag": False, "waffles": 5}
    initattributes = attributes.copy()  # Call the copy method
    def resetAttributes():
        nonlocal attributes 
        nonlocal initattributes
        attributes = initattributes.copy()  # Copy again to reset to the initial state

    print(attributes)
    attributes["waffles"] = 4
    print("init:" + str(initattributes))
    print(attributes)
    resetAttributes()
    print("this suppose to be 5")
    print(attributes)

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