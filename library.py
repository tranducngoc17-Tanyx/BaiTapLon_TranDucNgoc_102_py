from book import Book
from student import Student

class Library:
    def __init__(self):
        self.books = []
        self.students = []

    def add_book(self):
        id = input("Nhập mã sách: ")
        title = input("Nhập tên sách: ")
        author = input("Nhập tác giả: ")

        while True:
            try:
                quantity = int(input("Nhập số lượng: "))
                if quantity < 0:
                    print("Số lượng không được âm!")
                else:
                    break
            except ValueError:
                print("Số lượng phải là số nguyên!")

        self.books.append(Book(id, title, author, quantity))
        print("Thêm sách thành công!")

    def view_books(self):
        if len(self.books) == 0:
            print("Chưa có sách!")
            return

        print("\nDanh sách sách:")
        for book in self.books:
            book.show_info()

    def search_book(self):
        id = input("Nhập mã sách cần tìm: ")

        for book in self.books:
            if book.id == id:
                print("Đã tìm thấy sách:")
                book.show_info()
                return

        print("Không tìm thấy sách!")

    def delete_book(self):
        id = input("Nhập mã sách cần xóa: ")

        for book in self.books:
            if book.id == id:
                self.books.remove(book)
                print("Xóa sách thành công!")
                return

        print("Không tìm thấy sách!")

    def add_student(self):
        id = input("Nhập mã sinh viên: ")
        name = input("Nhập họ tên: ")
        class_name = input("Nhập lớp: ")

        self.students.append(Student(id, name, class_name))
        print("Thêm sinh viên thành công!")

    def view_students(self):
        if len(self.students) == 0:
            print("Chưa có sinh viên!")
            return

        print("\nDanh sách sinh viên:")
        for student in self.students:
            student.show_info()

    def search_student(self):
        id = input("Nhập mã sinh viên cần tìm: ")

        for student in self.students:
            if student.id == id:
                print("Đã tìm thấy sinh viên:")
                student.show_info()
                return

        print("Không tìm thấy sinh viên!")

    def delete_student(self):
        id = input("Nhập mã sinh viên cần xóa: ")

        for student in self.students:
            if student.id == id:
                self.students.remove(student)
                print("Xóa sinh viên thành công!")
                return

        print("Không tìm thấy sinh viên!")

    def borrow_book(self):
        student_id = input("Nhập mã sinh viên: ")
        book_id = input("Nhập mã sách: ")

        student = None
        book = None

        for std in self.students:
            if std.id == student_id:
                student = std

        for bk in self.books:
            if bk.id == book_id:
                book = bk

        if student is None:
            print("Không tìm thấy sinh viên!")
            return

        if book is None:
            print("Không tìm thấy sách!")
            return

        if book.borrow():
            print("Mượn sách thành công!")
        else:
            print("Sách đã hết!")

    def return_book(self):
        book_id = input("Nhập mã sách cần trả: ")

        for book in self.books:
            if book.id == book_id:
                book.return_book()
                print("Trả sách thành công!")
                return

        print("Không tìm thấy sách!")