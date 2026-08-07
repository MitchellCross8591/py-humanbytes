import unittest

from humanbytes import format_bytes, parse_bytes


class HumanBytesTest(unittest.TestCase):
    def test_units(self):
        self.assertEqual(format_bytes(0), "0B")
        self.assertEqual(format_bytes(1536), "1.5KB")
        self.assertEqual(format_bytes(1048576), "1.0MB")

    def test_parse_units(self):
        self.assertEqual(parse_bytes("0B"), 0)
        self.assertEqual(parse_bytes("1.5KB"), 1536)
        self.assertEqual(parse_bytes(" 1 mb "), 1048576)

    def test_parse_rejects_invalid_values(self):
        with self.assertRaises(ValueError):
            parse_bytes("1.5")
        with self.assertRaises(TypeError):
            parse_bytes(1024)


if __name__ == "__main__":
    unittest.main()
