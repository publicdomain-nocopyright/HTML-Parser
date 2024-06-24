
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
        if not htmltag:
            if not start_text:  
                text = '<text>'
                start_text = True
            
        if not htmltag:  
            text += letter

    if text:  
        text += '</text>'
        tokens.append(text)
    
    print(tokens)


def simplestatemachine():
    pass