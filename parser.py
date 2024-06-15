print("Welcome to the HTML Parser")

print(open("example.html").read())

print("__________________")

print("Tokenization")
tokens = {}
with open("example.html") as file:
    content = file.read().replace(" ", "").replace("\n", "").replace("\t", "")
    print(content)
    #for line in file:
    #    print(line)
        #key, value = line.split('')


input()