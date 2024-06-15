try: 
    print("Welcome to the HTML Parser")
    print("HTML parsing is the process of taking raw HTML code, reading it, and generating a DOM tree object structure from it.")

    print(open("example.html").read())

    print("__________________")

    print("Tokenization")

    tokens = {}
    with open("example.html") as file:
        content = file.read().replace(" ", "").replace("\n", "").replace("\t", "")
        print(content)
    print("Note: The HTML5 Doctype requires an ASCII space.")
    print("__________________")


    def htmlfiletostring(htmlfile, html=""):
        with open(htmlfile) as file:
            for line in file.read().replace("\n", ""):
                    for letter in line:
                        html += letter 
                        if letter == " ":
                            print("|_|", end="")
                        else:
                            print(letter, end="")
        print()
        return html
        print("\nNote: Now Detects ASCII spaces")

    def htmltotokens(htmlstring):
        for letter in htmlstring:
            print(letter, end="")
        pass

    print()
    print(htmltotokens(htmlfiletostring("example.html")))
    input()
except Exception as e:
    print(e)