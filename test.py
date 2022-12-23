from test_encryption import *

def test():
    a = ' som '
    x = encryption(a)
    y = decryption(x)
    assert y == a

test()
