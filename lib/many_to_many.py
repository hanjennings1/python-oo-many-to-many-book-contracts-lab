class Author:
    all = []        # tracks every Author instance created

    def __init__(self, name):
        self.name = name
        Author.all.append(self)       # register this author in the class list

    def contracts(self):
            # all contracts where this author is the one that's in the contract
             return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
    # create and return a new Contract
        return Contract(self, book, date, royalties)


class Book:
    all = []        # tracks every Book instance created

    def __init__(self, title):
        self.title = title
        Book.all.append(self)       # register this book in the class list

    def contracts(self):
        # all contracts where this book is the one that's under contract
         return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        # authors tied to this book, based on its contract(s)
        return [contract.author for contract in self.contracts()]


class Contract:
    all = []        # tracks every Contract instance created

    def __init__(self, author, book, date, royalties):
        # shows error message if any input is invalid:
        if not isinstance(author, Author):         
            raise Exception("Invalid author")
        if not isinstance(book, Book):
            raise Exception("Invalid book")
        if not isinstance(date, str):
            raise Exception("Invalid date")
        if not isinstance(royalties, int):
            raise Exception("Invalid royalties")
         
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)       # register this contract in the class list

    @classmethod
    def contracts_by_date(cls, date):
         return [contract for contract in cls.all if contract.date == date]
    