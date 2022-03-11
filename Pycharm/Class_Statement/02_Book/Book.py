"""
@Author : Rohit Shedage
@Goal : To implement Book Class
"""


class Book:
    """
    This is Book Class Contain various property
    """
    def __init__(self, init_bk_title: str, init_bk_author: list,
                 init_bk_publication: str, init_bk_genre: str,
                 init_bk_nr_pages: int, init_bk_edition: int,
                 init_bk_reprint: int, init_bk_isbn: str,
                 init_bk_price: float
                 ):

        """
        Parameterized Constructor of Book Class
        :param init_bk_title: Title of Book type string
        :param init_bk_author: Authors of Book type list
        :param init_bk_publication: Publication of Book type string
        :param init_bk_genre: Genre of Book type string
        :param init_bk_nr_pages: Number of Pages in Book type integer
        :param init_bk_edition: Number of Edition of Book type integer
        :param init_bk_reprint: Count of reprint of Book type integer
        :param init_bk_isbn: Number of ISBN of Book string
        :param init_bk_price: Price of Book in float
        """
        self.bk_title = init_bk_title
        self.bk_author = init_bk_author
        self.bk_publication = init_bk_publication
        self.bk_genre = init_bk_genre
        self.bk_nr_pages = init_bk_nr_pages
        self.edition = init_bk_edition
        self.bk_edition = self.edition
        self.bk_reprint = init_bk_reprint
        self.bk_isbn = init_bk_isbn
        self.bk_price = init_bk_price


b = Book("Introduction of Alorithm", ['Corem', 'Leiseron', 'Rivet'], 'MITPRESS', 'Algorithm', 1292, 3, 1, "978-0-062-03384-8", 3500)


print(b.__dict__)