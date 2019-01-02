from unittest import TestCase

from validate_india import mobile, aadhaar, pan


class TestMobile(TestCase):
    def test_mobile_1(self):
        self.assertTrue(mobile.is_valid('8698009017'))

    def test_mobile_2(self):
        self.assertTrue(mobile.is_valid('+91 8698009017'))

    def test_mobile_3(self):
        self.assertFalse(mobile.is_valid('2410121233'))


class TestAadhaar(TestCase):
    def test_aadhaar_1(self):
        self.assertTrue(aadhaar.is_valid('444455556666'))

    def test_aadhaar_2(self):
        self.assertTrue(aadhaar.is_valid('4444 5555 6666'))

    def test_aadhaar_3(self):
        self.assertFalse(aadhaar.is_valid('22132112'))


class TestPAN(TestCase):
    def test_pan_1(self):
        self.assertTrue(pan.is_valid('BLEPM0021Q'))

    def test_pan_2(self):
        self.assertFalse(pan.is_valid('ABCSDWW123'))
