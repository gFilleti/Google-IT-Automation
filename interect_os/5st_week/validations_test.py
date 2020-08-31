#!/usr/bin/env python3.8

import unittest

from validations import validate_user

class TestValidateUser(unittest.TestCase):

    def test_valid(self):
        self.assertEqual(validate_user("validuser", 3), True)

    def test_too_short(self):
        self.assertEqual(validate_user("inv", 5), False)

    def test_invalid_characters(self):
        self.assertEqual(validate_user("invalid_user", 1), False)

    def test_invalid_minlen(self):
        self.assertRaises(ValueError, validate_user, "user", -1)
        #this method frist need the  error type
        # than the function name followed by any paramters that need to be passed to that function
        #this  method its calling the function that we want to test using a try except block to checking that it does raise the error
        #that we said it would raise.

# RUn the tests

unittest.main()
