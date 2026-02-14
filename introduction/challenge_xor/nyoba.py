from pwn import *

key1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313") # bytes.fromhex() decodes hex to byte
key1_2 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
key2_3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
flag_1_2_3 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

#pembatas 

Key2 = "911404e13f94884eabbec925851240a52fa381ddb79700dd6d0d"
Key_3 = "504053b757eafd3d709d6339b140e03d98b9fe62b84add0332cc"
Key_1_XOR_Key_2_XOR_Key_3 = "679ce12554e557ada0e38f2e52f126e54240b2576c83c4196cd2"

flag= xor(bytes.fromhex(flag_1_2_3), bytes.fromhex(Key_1_XOR_Key_2_XOR_Key_3))

print(flag.decode())