# lab03.py
# Luis Valdivia and Cassidy Block, Feb.20, 2018
# a cipher function and test cases

import pytest

#a general Caesar cipher that shifts a message by n positions
def rot(n, message):
    output = ""
    for i in message:
        output += chr((ord(i)- ord('a')+n) % 26 + ord('a'))
    return output


#test cases
def test_apple1():
   assert rot(1,"apple") == "bqqmf" 

def test_apple2():
   assert rot(2,"apple") == "crrng" 

def test_appleInv():
   assert rot(-2,rot(2,"apple")) == "apple" 
