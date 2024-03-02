#!/usr/bin/env python3
import base64 as b64
from pwn import *



KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
KEY2 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
KEY3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
r = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

key1 = bytes.fromhex(KEY1)
key2xorkey1= xor(bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"), key1)
k3= xor(bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"),key2xorkey1)
k3xork2= xor(k3,key2xorkey1)
flag = xor(key1,k3xork2)
final = xor(flag, bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"))
print(final)


