#!/usr/bin/env python3.8

from rearrange import rearrange_name
import unittest# this module provides a test case class with a bunch of testing methods

class TestRearrange(unittest.TestCase):
#To access this functionality, we create out own classe by inherits from test case, thus inheriting all those testing methods
# this class will inheits funtionality from the TestCase class located in unit test module
#Any methods we define in out TestRearrange class that start with the prefix test will automatically become tests tha can
#be run by the tsting framework.

    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)#this method provided to us by the TestCase class we inhereted from to verify
                                                            #that what we wxpected is exactly what we got.
                                                            #The assertEqual method basically says both of my arguments are equal

    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)
        #this test its a Edge case, Edge cases are imputs to our code that produce unexpected results, and are found at the extreme ends of the ranges
        #of  input we imagine our programs will typically work with
        #we can handle this edge case by preforming a simple check of the result variable before operating with it

    def test_doble_name(self):
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_one_name(self):
        testcase = "Volteire"
        expected = "Volteire"
        self.assertEqual(rearrange_name(testcase), expected)



unittest.main()
