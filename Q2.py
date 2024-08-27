from typing import List, Iterable
from data_structures.array_sorted_list import ArraySortedList
from book import Book

def get_books(books: ArraySortedList[Book], start_year: int) -> Iterable[str]:
	# Get index. Remember: assignments prohibit you from accessing private members/methods (i.e. those that are prefix with '_')
	dummy = Book("", start_year, "")
	books.add(dummy)
	idx = books.index(dummy)
	books.remove(dummy) # remove dummy added

	for i in range(idx, len(books)):
		yield books[i].publication_year


if __name__ == "__main__":
	pass