from library import Library

def menu():
    print("========== LIBRARY MANAGEMENT ==========")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Add Student")
    print("6. View Students")
    print("7. Search Student")
    print("8. Delete Student")
    print("9. Borrow Book")
    print("10. Return Book")
    print("0. Exit")


def main():
    library = Library()

    while True:
        menu()
        choice = input("Choose: ")

        match choice:
            case "1":
                library.add_book()

            case "2":
                library.view_books()

            case "3":
                library.search_book()

            case "4":
                library.delete_book()

            case "5":
                library.add_student()

            case "6":
                library.view_students()

            case "7":
                library.search_student()

            case "8":
                library.delete_student()

            case "9":
                library.borrow_book()

            case "10":
                library.return_book()

            case "0":
                print("Goodbye!")
                break

            case _:
                print("Invalid choice!")

main()