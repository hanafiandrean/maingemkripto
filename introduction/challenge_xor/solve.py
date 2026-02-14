from pwn import *

ch = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

def is_mostly_printable(s):
    printable = sum(1 for c in s if 32 <= c <= 126)
    return printable / len(s) > 0.9

for key in range(256):
    decrypted = bytes(c ^ key for c in ch)
    if is_mostly_printable(decrypted):
        if b"crypto" in decrypted:
            print("Key:", key)
            print("Decrypted:", decrypted.decode())



