text = "label"

key = 13

print("crypto{", end="")

for char in text:
    encoded = chr(ord(char) ^ key) 
    print(encoded)

print("}")
