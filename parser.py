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

    from itertools import cycle
    tag_mark = cycle([True, False])
            

    # find the '<', lock up until next time called, 'unlock' when encountering '>' but include as well.
    # The cycle technique does not have enforcement of < matching the > tagmark and would go over and mix up.
    # Aka, what if next tag mark is < <> >, That's double opening tag.
    def addup():
        yield tag_mark 
        

        yield letter 
        letter = ''
        pass
    
    def tokenize():
        tag = False
        for letter in htmlstring:            
            # if letter == '<' or letter == '>': add(letter)
            # if letter == '<' or letter == '>': scan(letter)
            if letter == '<' or letter == '>': tag = next(tag_mark)
            if tag:
                print(letter, end="")

                #start_tokenization()
            #else:


            #if tag_mark:
                #stop_tokenization()
                #print(tokenization['tokens'], end="")
                #tokenization['tokens'].append( [tokenization["token"], tokenization["attributes"]] )

            #if tokenization['tokenizing']: 
            #   tokenization['token'] += letter

        return tokenization["tokens"]
    return tokenize()

            #    if letter == '/':
            #        tokenization["attributes"]["is_closing_tag"] = True

            #if letter == '>':
            #    stop_tokenization()
            #    tokenization['tokens'].append( [tokenization["token"], tokenization["attributes"]] ); 

            #if not tokenization['tokenizing']:
            #    if letter != '>' or letter != '<':
            #        texttag=True
                    #print(letter, end="")


            

        



tokens = htmltotokens(parser_library.htmltostring("example.html"))

import pprint
pprint.pprint(tokens)
    