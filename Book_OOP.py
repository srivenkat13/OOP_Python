#  define a book Class with name , technology, Edition and author


class Book:
    def __init__(self, name, technology, edition, author):
        self.bookName = name
        self.bookTechnology = technology
        self.bookEdition = edition
        self.bookAuthor = author


# create a Class Bookstore with bookdb   attribute
#  bookbd is a dictionary with a key value pair of  serial nummber of book and Book object ( the class above is )

#  then define two methods in the bookstore Class as SearchByTechnology and BooksWithMoreThanTwoEditions
class Bookstore:
    def __init__(self, bookdict):
        self.bookdb = bookdict

    def searchByTechnology(self, technology):
        """
        searchByTechnology: this method will find the respective book object based on the technology of the book supplied as an argument; from the dictionary of book objects and return the list of book objects who techonolgy matches with the argument passed.

        If there is no book found with the given arugment it will return a NULL objects i.e.,None in python
        """
        matchedBooks = []  # this is a list to store the results
        flag = 0

        for i in self.bookdb.keys():
            if technology == self.bookdb[i].bookTechnology:
                matchedBooks.append(self.bookdb[i])
                flag = 1

        if flag == 0:
            return None

        return matchedBooks

    def booksWithMoreThanTwoEditions(self):
        """
        This method will return the number of books whose editon is two or more than two.

        If no book is found it should return 0
        ( both these methods will be called from the main section)
        """
        bookcount = 0  # to store the number of books that are greater than edition 2
        for i in self.bookdb.keys():
            if self.bookdb[i].bookEdition >= 2:
                bookcount += 1

        return bookcount


""" start the main fucntion here """

if __name__ == "__main__":
    bookdb = {}
    bookCountMaster = int(input())
    for i in range(bookCountMaster):
        name = input()
        technology = input()
        edition = int(input())
        author = input()
        bookObj = Book(name, technology, edition, author)
        bookdb.update({i: bookObj})
    
    bookStoreObj = Bookstore(bookdb)

    # the input for what to search from the book techonology 
    bookTechnologySearchFor=input()

# all the inputs are taken till this line. next calling the methods 

    matchedBooks=bookStoreObj.searchByTechnology(bookTechnologySearchFor)

    bookcount=bookStoreObj.booksWithMoreThanTwoEditions()

#  now printing the output , if condition has edge cases  and else has normal output
    if matchedBooks==None:
        print('No book exists with the given technology')
    else:
        for j in matchedBooks:
            print(j.bookName)
            print(j.bookTechnology)
            print(j.bookEdition)
            print(j.bookAuthor)
    
    if bookcount==0:
        print('No book is having greater than two editions')
    else:
        print(bookcount)
