class Book:
    def __init__(self,name,technology,edition,author):
        self.bookName = name
        self.bookTechnology = technology
        self.bookEdition = edition
        self.bookAuthor = author

class Bookstore:
    def __init__(self,bookdict):
        self.bookdb =bookdict
    
    def searchByTechnology(self,technology):
        booksMatched=[]
        flag = 0

        for i in self.bookdb.keys():
            if (technology== self.bookdb[i].bookTechnology):
                booksMatched.append(self.bookdb[i])
                flag =1
            
        if flag == 0:
            return None
        
        return booksMatched
    
    def booksWithMoreThanTwoEditions(self):
        bookcount = 0

        for i in self.bookdb.keys():
            if (self.bookdb[i].bookEdition >= 2):
                bookcount += 1

        return bookcount

if __name__ =="__main__":
    bookdb={}
    bookcounterMaster=int(input())
    for i in range(bookcounterMaster):
        name= input()
        technology = input()
        edition = int(input())
        author= input()
        bookObj = Book(name,technology,edition,author)
        bookdb .update({i:bookObj})

    bookstoreObj = Bookstore(bookdb)

    bookTechnologySearchfor = input()

    matchedBooks= bookstoreObj.searchByTechnology(bookTechnologySearchfor)

    bookcount = bookstoreObj.booksWithMoreThanTwoEditions()

    if matchedBooks == None:
        print('No books exists with the give technology')
    else:
        for j in matchedBooks:
            print(j.bookName)
            print(j.bookTechnology)
            print(j.bookEdition)
            print(j.bookAuthor)

    if bookcount == 0:
        print(' There are no books with more than two editions')
    else:
        print(bookcount)