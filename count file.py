with open('input.txt','w') as f:
    f.write("python is fun\n let's count lines,words, and characters!")
with open('input.txt','r') as f:
    lines=f.readlines()
line_count=len(lines)
word_count = sum(len(line.split()) for line in lines)
char_count = sum(len(line) for line in lines)
print("lines: ",line_count)
print("words: ",word_count)
print("characters: ",char_count)