class Library:
    def __init__(self):
        self.book_collection={}
    def display(self):
        print("welcome to our library",end="\n")
        print("this is our collection of books")
        print(self.book_collection)
    def collection(self):
        self.book_collection["Harry potter"]=5
        self.book_collection["It ends with us"]=3
        self.book_collection["atomic habits"]=10
    def borrow_book(self,book_name):
        if book_name in self.book_collection:
            if self.book_collection[book_name] !=0:
                self.book_collection[book_name] -=1
                print("here is your book")
            else:
                print("currently not available")
        else:
            print("we dont have that book")
    def return_book(self,book_name):
        if book_name in self.book_collection:
            self.book_collection[book_name]+=1 
            print("thanks for returning")
        else:
            self.book_collection[book_name]=1
            print("thanks for donating new book")
