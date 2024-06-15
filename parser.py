try: 
    print("Welcome to the HTML Parser")

    print(open("example.html").read())

    print("__________________")

    print("Tokenization")

    tokens = {}
    with open("example.html") as file:
        content = file.read().replace(" ", "").replace("\n", "").replace("\t", "")
        print(content)
    print("Note: The HTML5 Doctype requires an ASCII space.")
    print("__________________")

    with open("example.html") as file:
        for line in file.read().replace("\n", ""):
                for letter in line:
                    if letter == " ":
                        print("|_|", end="")
                    else:
                         print(letter, end="")
     print("\nNote: Now Detects ASCII spaces")




    input()
except Exception as e:
    print(e)