import unittest
from Q1 import max_nesting 
from ed_utils.decorators import number


class Test_Q1(unittest.TestCase):
    @number("1.1")
    def test_examples(self):
        self.assertEqual(max_nesting("(1+(2*3)+((8)/4))+1"), 3)
        self.assertEqual(max_nesting("(1)+((2))+(((3)))"), 3)
        
    @number("1.2")
    def test_extra(self):
        self.assertEqual(max_nesting("(()()()())"), 2)
        self.assertEqual(max_nesting("()()()()"), 1)
        self.assertEqual(max_nesting("(((())))"), 4)

if __name__ == '__main__':
    unittest.main()