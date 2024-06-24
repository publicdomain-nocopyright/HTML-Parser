
from parser_library import *


def tokenizer():
    token = ''
    tokens = []
    htmltag = False

    for letter in htmltostring("example.html"):
        
        if letter == '<': htmltag = True; continue
        if letter == '>': htmltag = False; tokens.append(token); token=''; continue
        if htmltag:
            token += letter
            
        #print(letter, end="")
        pass
    print(tokens)


@execute
def tokenizer():
    token = ''
    tokens = []
    htmltag = False
    text = ''
    start_text = False  

    #TODO: Match tag with another tag by tag nest level.
    for letter in htmltostring("example.html"):

        if letter == '<' and text:
            if text:  
                text += '</text>'
                tokens.append(text)
                text = ''
            start_text = False  

        if letter == '<': htmltag = True; continue
        if letter == '>': htmltag = False; tokens.append(token);token = '' ; continue           
        
        if htmltag:
            token += letter

        if not htmltag and not start_text:
            text = '<text>'
            start_text = True
            
        if not htmltag and start_text:  
            text += letter

    if text:  
        text += '</text>'
        tokens.append(text)
    
    print(tokens)


def simplestatemachine():
    pass