from pwn import *

key1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313") # bytes.fromhex() decodes hex to byte
key1_2 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
key2_3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
flag_1_2_3 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

key2 = xor(bytes.fromhex(key1_2), key1)
#hasil XOR dari key1_2 dan key1 akan menghasilkan key2 = 911404e13f94884eabbec925851240a52fa381ddb79700dd6d0d
key3 = xor(bytes.fromhex(key2_3), key2)
#hasil XOR dari key2_3 dan key2 akan menghasilkan key3 = 504053b757eafd3d709d6339b140e03d98b9fe62b84add0332cc
key123 = xor(bytes.fromhex(key1_2), key3)
#hasil XOR dari key1_2 dan key3 akan menghasilkan key123 = 679ce12554e557ada0e38f2e52f126e54240b2576c83c4196cd2
flag= xor(bytes.fromhex(flag_1_2_3), key123)

print(flag.decode())
print("Key 2:", key2.hex())
print("Key 3:", key3.hex())
print("Key 1 XOR Key 2 XOR Key 3:", key123.hex())