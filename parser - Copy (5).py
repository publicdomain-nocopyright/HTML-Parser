import parser_library

# Tokenization is needed to easily select tokens and group, target them against other tokens.
# Associate p start tag with p end tag. 

class tokenizer():
    def __init__(self):
        self.tokenization = False

    def begintokenization(self):
        self.tokenization = True

    def stoptokenization(self):
        self.tokenization = False

    def htmltotokens(self, htmlstring, token="", closingtag=False):
        for letter in htmlstring:
            if letter == '<': self.begintokenization(); continue
            if letter == '>': self.stoptokenization(); print(token, closingtag); token = ""; 
                
            if self.tokenization: token += letter
            if self.tokenization and letter == "/": closingtag = True

tokenizer().htmltotokens(parser_library.htmltostring("example.html"))

print()
print("Tokenization")