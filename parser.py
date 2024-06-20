# parser.py - main project file.
#   Tokenization is the process of splitting text into smaller units called tokens, typically words or phrases, for further analysis.
import parser_library


# Tokenization is needed to easily select tokens and group, target them against other tokens.
# Associate p start tag with p end tag. 
# TODO: Tags nesting support and text association with tags.



def htmltotokens(htmlstring : str = None):
    token  : str = None
    tokens : list[str] = []
    letter : str = None


    # Tokenization definition, Capture tokens
    tokenization : dict[str,any]
    tokenization = {
    'state'     : 'stopped',
    'tokenizing':  False,
    'token'     :  None,
    'tokens    ':  [],
    'attributes':  default_attributes.copy()
    }

    def start_tokenization():
        tokenization['state'] = 'running'
        tokenization['tokenizing'] = True
        tokenization['token'] = None #reset_token
        tokenization['attributes'] = default_attributes.copy() #reset_attributes

    def stop_tokenization():
        tokenization['state'] = 'stopped'
        tokenization['tokenizing'] = False
        tokenization['tokens'].append((tokenization[token], tokenization[attributes])); 
        
    for letter in htmlstring:
        if letter is '<':
            start_tokenization()

        if tokenization['tokenizing']: 
            tokenization['token'] += letter

        if letter is '>':
            stop_tokenization()

    default_attributes : dict[str, any] = {"is_closing_tag": False, "test": True} 
    attributes : dict[str, any] = default_attributes.copy()

    tokenizing : bool = False

    # Tag Scanning, processing, tokenization, html tag-markers (<>) and tag-name (<somename>) capture
    for letter in htmlstring:
        if letter is '<': # Trigger tokenization
            tokenizing = True 
            token = None; 
            attributes = default_attributes.copy();
            continue
        

        if tokenizing:
            if token is None: token = "" 
            if letter is '>': tokenizing = not tokenizing; 

            if token is not None and letter is not '>':
                token += letter
                if letter == '/':
                    attributes["is_closing_tag"] = True
            
        else:
            print(letter)

        if not tokenizing and token is not None:
            tokens.append((token, attributes)); 
            tokenizing = False
            token = None
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