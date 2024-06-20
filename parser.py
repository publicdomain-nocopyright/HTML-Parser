# parser.py - main project file.
#   Tokenization is the process of splitting text into smaller units called tokens, typically words or phrases, for further analysis.
import parser_library


# Tokenization is needed to easily select tokens and group, target them against other tokens.
# Associate p start tag with p end tag. 
# TODO: Tags nesting support and text association with tags.



def htmltotokens(htmlstring : str = None):

    default_attributes : dict[str, any] = {"is_closing_tag": False, "test": True} 


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
        nonlocal tokenization
        tokenization['state'] = 'running'
        tokenization['tokenizing'] = True
        tokenization['token'] = None #reset_token
        tokenization['attributes'] = default_attributes.copy() #reset_attributes

    def stop_tokenization():
        nonlocal tokenization
        tokenization['state'] = 'stopped'
        tokenization['tokenizing'] = False
        if 'tokens' not in tokenization:
            tokenization['tokens'] = []

        
        
    def tokenize():
        nonlocal tokenization
        for letter in htmlstring:
            if letter == '<':
                start_tokenization()

            if tokenization['tokenizing']: 
                if tokenization['token'] is None:
                    tokenization['token'] = ""
                tokenization['token'] += letter

            if letter == '>':
                stop_tokenization()
                tokenization['tokens'].append((tokenization["token"], tokenization["attributes"])); 
    tokenize()
    return tokenization["tokens"]
tokens = htmltotokens(parser_library.htmltostring("example.html"))

print(tokens)
    