with open('input.txt','w') as infile:
    infile.write("banana apple orange banana mango")
with open('input.txt','r') as infile:
    text=infile.read()
    print("original text from input.txt: ",text)
words = text.lower().split()
words.sort()
with open('output.txt','w') as outfile:
    sorted_text=''.join(words)
    outfile.write(sorted_text)
print("\n sorted and lower cased words writtern to output.txt")
print(sorted_text)