# parser.py - main project file.
#   Tokenization is the process of splitting text into smaller units called tokens, typically words or phrases, for further analysis.
import parser_library
from parser_library import exe


# Tokenization is needed to easily select tokens and group, target them against other tokens.
# Associate p start tag with p end tag. 
# TODO: Tags nesting support and text association with tags.



def htmltotokens(htmlstring : str = None):


    ###____________________Tokenizer_____________________###
    default_attributes : dict[str, any] = {"is_closing_tag": False} 

    # Tokenization definition, Capture tokens
    tokenization : dict[str,any]
    tokenization = {
    'state'     : 'stopped',
    'tokenizing':  False,
    'token'     :  None,
    'tokens'    :  [],
    'attributes':  default_attributes.copy()
    }

    def start_tokenization():
        tokenization['state'] = 'running'
        tokenization['tokenizing'] = True
        tokenization['token'] = "" 
        tokenization['attributes'] = default_attributes.copy() 

    def stop_tokenization():
        tokenization['state'] = 'stopped'
        tokenization['tokenizing'] = False

    def textsweeping():
        # Text sweeping is a technique of reading letters from one tag until another enclosing tag is met.
        pass

    
    def tokenize():
        texttagopen = False
        texttag= False
        for letter in htmlstring:
            if letter == '<':
                start_tokenization()

            if tokenization['tokenizing']: 
                tokenization['token'] += letter
                if letter == '/':
                    tokenization["attributes"]["is_closing_tag"] = True

            if letter == '>':
                stop_tokenization()
                tokenization['tokens'].append( [tokenization["token"], tokenization["attributes"]] ); 
    
            if not tokenization['tokenizing']:
                if letter != '>':
                    texttag=True
                    #print(letter, end="")
                if texttag:
                    tokenization['token'] = "<text>"
                    texttag = False
                    texttagopen = True
                if texttagopen:
                    tokenization['token'] += letter
                if letter == '>' and texttagopen:
                    tokenization['token'] += "</text>"
                    texttagopen = False
                    tokenization['tokens'].append( [tokenization["token"], tokenization["attributes"]] ); 

            


            

        return tokenization["tokens"]

    return tokenize()

tokens = htmltotokens(parser_library.htmltostring("example.html"))

import pprint
pprint.pprint(tokens)
    