import unittest
from logic.decoder import decode_catalog_number

class TestDecoder(unittest.TestCase):
    def test_decode(self):
        result = decode_catalog_number("10250T-A1")
        self.assertIn("decoded", result)

if __name__ == "__main__":
    unittest.main()
