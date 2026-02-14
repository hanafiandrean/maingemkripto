from pwn import *

key1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313") # bytes.fromhex() decodes hex to byte
key1_2 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
key2_3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
flag_1_2_3 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

key2 = xor(bytes.fromhex(key1_2), key1)
key3 = xor(bytes.fromhex(key2_3), key2)
# xor (a,b) 
# sebelum di xor, pastikan untuk mendekode dari hex ke bytes dengan menggunakan bytes.fromhex()
# cari atau decode key secara berurutan, karena sifat XOR yang komutatif dan asosiatif, kita bisa mencari key dengan urutan apapun, tapi untuk memudahkan kita bisa mencari key secara berurutan

key123 = xor(bytes.fromhex(key1_2), key3)

#setelah mendapatkan key123, kita bisa mencari flag dengan cara XOR antara flag_1_2_3 dengan key123
flag= xor(bytes.fromhex(flag_1_2_3), key123)

print(flag.decode())


# Commutative: A ⊕ B = B ⊕ A
# Associative: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C
# Identity: A ⊕ 0 = A
# Self-Inverse: A ⊕ A = 0

# ⊕ artinya = XOR (exclusive OR) 

# challenge : Before you XOR these objects, be sure to decode from hex to bytes. 
# artinya : Sebelum kamu XOR objek-objek ini, pastikan untuk mendekode dari hex ke bytes.