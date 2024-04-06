class Book:
    def __init__(self, book_title: str, publication_year: int, author: str):
        self.book_title = book_title
        self.publication_year = publication_year
        self.author = author
    

    # Small preview of what Encapsulation, not required for this Weeks coding activity
    # def get_book_title(self) -> str:
    #     return self.__book_title
    
    # def set_book_title(self, book_title: str):
    #     self.book_title = book_title
    
    # def get_publication_year(self) -> int:
    #     return self.publication_year
    
    # def set_publication_year(self, publication_year: int):
    #     self.publication_year = publication_year
    
    # def get_author(self) -> str:
    #     return self.author
    
    # def set_author(self, author: str):
    #     self.author = author