#initilize the list, set and dictionary
books_lists=[]
author_sets=set()
books_dict={}
books_lists.append("Python Programming")
author_sets.add("John smith")
books_dict["Python programming"]="John smith"

books_lists.append("Data structure and Algorithm")
author_sets.add("Jane Doe")
books_dict["Data structure and Algorithm"]="Jane Doe"

books_lists.append("Machine learning Basics")
author_sets.add("Alice Johnson")
books_dict["Machine learning Basics"]="Alice Johnson"
#serching the books
search_title=input("Enter the Books\'s title:")
if search_title in books_lists:
          print(f"Book found! Author:{books_dict[search_title]}")
else:
          print("Books not found!")
          #Displaying the list
print("List of the Books")
for book in books_lists:
          print(book)
          # Removing thr book from the list
remove_title=input("Enter the book title to remove or enter to skip")
if remove_title in books_lists:
          remove_author=books_dict[remove_title]
          books_lists.remove(remove_title)
          author_sets.remove(remove_author)
          del books_dict[remove_title]
          print("Book remove successful ")
          #print("Books available ",books_lists)
else:
          print("Book not found")
print("Books available ",books_lists)