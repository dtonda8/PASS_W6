import unittest
from Q2 import get_books
from ed_utils.decorators import number
from tests.conversions import ListtoSL
from book import Book
from typing import Iterable


class Test_Q2(unittest.TestCase):
    def assertResultEqual(self, actual: Iterable, expected: Iterable):
        if sum(1 for _ in actual) != sum(1 for _ in expected):
            self.fail("Length doesn't match expected length")

        for e, a in zip(expected, actual):
            if e != a:
                self.fail(f"Results did not match, expected: {e}, actual: {a}")
        
        
    @number("2.1")
    def test_examples(self):
        books = [
            Book("Nineteen Eighty-Four", 1949, "George Orwell"), 
            Book("To Kill a Mockingbird", 1960, "Harper Lee"), 
            Book("The Handmaid's Tale", 1985, "Margaret Atwood"), 
            Book("The Da Vinci Code", 2003, "Dan Brown"), 
            Book("The Road", 2006, "Cormac McCarthy")
        ]
        expected = iter(["The Handmaid's Tale", "The Da Vinci Code", "The Road"])
        self.assertResultEqual(get_books(ListtoSL(books), 1984), iter(expected))

    @number("2.2")
    def test_extra(self):
        books = [
            Book("The Great Gatsby", 1925, "F. Scott Fitzgerald"),
            Book("Brave New World", 1932, "Aldous Huxley"),
            Book("1984", 1949, "George Orwell"),
            Book("The Catcher in the Rye", 1951, "J.D. Salinger"),
            Book("Harry Potter and the Philosopher's Stone", 1997, "J.K. Rowling")
        ]
        expected = ["The Catcher in the Rye", "Harry Potter and the Philosopher's Stone"]
        self.assertResultEqual(get_books(ListtoSL(books), 1950), iter(expected))
        

if __name__ == '__main__':
    unittest.main()