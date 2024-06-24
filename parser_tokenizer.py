
from parser_library import *
#INFO: HTML Tag: <somename> Consist of: <> tag markers and tag-name: somename
#INFO: HTML Tag can have a HTML Attribute with <somename attribute=""> and without <somename attribute> value assignment
#TODO: Match Tag with another Tag by Tag-Nesting-level.

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


#DONE: capture text in <text> tags
@execute
def tokenizer():
    token = ''
    tokens = []
    htmltag = False
    text = ''
    start_text = False  

    for letter in htmltostring("example.html"):

        if letter == '<':
            htmltag = True
            if text:
                tokens.append('<text>' + text + '</text>')
                text = ''
            continue

        if letter == '>':
            htmltag = False
            tokens.append(token)
            token = ''
            continue

        if htmltag:
            token += letter
        else:
            if not start_text:
                start_text = True
                text = ''
            text += letter

    if text:
        tokens.append('<text>' + text + '</text>')
    
    print(tokens)





def simplestatemachine():
    pass