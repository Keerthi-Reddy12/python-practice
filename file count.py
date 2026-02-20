with open('input.txt','w') as f:
    f.write("hello world\n python prgramming\n file handling")
with open('input.txt','r') as f:
    lines = f.readlines()
print("reversed lines: ")
for line in lines:
    print(line.strip()[::-1])