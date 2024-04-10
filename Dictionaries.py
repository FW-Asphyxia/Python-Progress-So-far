output = ""
Message = input("> ")
Converter = {
    ":(": "😊",
    ":)": "😔",
    ":O": "😮",
     }

Words = Message.split(" ")
for Word in Words:
    output += Converter.get(Word, Word) + " "
print(output)
