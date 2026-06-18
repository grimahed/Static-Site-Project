from main import extract_title
import unittest

class test_main(unittest.TestCase):
    
    def test_heading_extraction(self):
        md = """# Hello"""


        head_line = extract_title(md)
        self.assertEqual(
            head_line,
            "Hello"
        )
        print("---EXTRACTION TEST---\n")
        print(head_line)
        print("\n-------------\n")





if __name__ == "__main__":
    unittest.main()