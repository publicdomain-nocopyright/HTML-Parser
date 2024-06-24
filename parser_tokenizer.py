
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

        if not htmltag and start_text == False:
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