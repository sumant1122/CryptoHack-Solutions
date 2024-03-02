#!/usr/bin/env python3
from pwn import *

label = "label"
print(xor(b'label', 13))