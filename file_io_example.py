with open('sample_text.txt') as file: # file is in local scope only
    text = file.read() # text is in global scope

print(text)
file.readlines()
