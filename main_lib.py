import library_1 
lib =library_1.Library()
lib.collection()
lib.display()
opt =int(input("want to return or borrow (enter 1 to return /enter 2 to borrow)"))
if opt ==1:
    name = input("enter the book name you want to return ")
    lib.return_book(name)
else:
    name = input("enter the book name you want to borrow ")
    lib.borrow_book(name)



