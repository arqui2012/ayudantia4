# -*- coding: UTF-8 -*-


import sys
# para Python 2.6 o inferior, utilizamos unittest2
if sys.hexversion < 0x2070000:
    import unittest2 as unittest
else:
    import unittest

import polish # el módulo a probar

class TestPolisher(unittest.TestCase):

    def test_tokenizer(self):
        tokens = [t for t in polish.tokenize("A * B + D * C")]
        expected = ["A","*","B", "+", "D","*", "C"]
        self.assertEquals(tokens, expected)

    def test_simple_addition(self):
        self.assertEquals(polish.polish("A + B"), "AB+")

    def test_multi_addition(self):
        self.assertEquals(polish.polish("A + B + C"), "ABC++")

    def test_simple_mult(self):
        self.assertEquals(polish.polish("A * B"), "AB*")

    def test_add_mult(self):
        self.assertEquals(polish.polish("A + B * C"), "ABC*+")

    def test_mult_add(self):
        self.assertEquals(polish.polish("A * B + C"), "AB*C+")

    def test_paren(self):
        self.assertEquals(polish.polish("(A + B) * C"), "AB+C*")
    def test_complex(self):
        self.assertEquals(polish.polish("(A + B) * (B + C * F)"), "AB+BCF*+*")

    def failed_test(self):
        self.fail()

if __name__ == '__main__':
    unittest.main(verbosity=2)