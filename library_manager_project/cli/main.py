
from library_manager.inventory import LibraryInventory
from library_manager.book import Book

inventory = LibraryInventory()

def menu():
    while True:
        print("\n==== Library Menu ====")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Search Book")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            inventory.add_book(Book(title, author, isbn))
            print("Book added!")

        elif choice == "2":
            isbn = input("Enter ISBN: ")
            book = inventory.search_by_isbn(isbn)
            if book and book.issue():
                inventory.save_data()
                print("Book issued!")
            else:
                print("Not available.")

        elif choice == "3":
            isbn = input("Enter ISBN: ")
            book = inventory.search_by_isbn(isbn)
            if book:
                book.return_book()
                inventory.save_data()
                print("Book returned!")
            else:
                print("Invalid ISBN.")

        elif choice == "4":
            for b in inventory.display_all():
                print(b)

        elif choice == "5":
            title = input("Enter title: ")
            results = inventory.search_by_title(title)
            for r in results:
                print(r)

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")

menu()
