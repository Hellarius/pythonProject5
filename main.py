def calc_average(numbers: list) -> float:
    for number in numbers:
        if not (isinstance(number, int) and isinstance(number, float)):
            raise ValueError("Invalid value in the list")

    return sum(numbers) / len(numbers)


def print_pyramid(rows: int):
    if not isinstance(rows, int):
        raise ValueError("Invalid value for rows")

    length = 1
    for row in range(rows):
        print("*" * length)
        length += 2


def clean_string(my_string: str) -> str:
    cleaned_string = re.sub("[^A-Za-z]+", '', my_string)
    return cleaned_string


def count_special_char(my_string: str) -> int:
    return len(my_string) - len(clean_string(my_string))


def dict_to_list(dictionary: dict) -> list:
    if len(dictionary) == 0:
        return []

    return list(dictionary.values())


def list_to_dict(key_list: list, value_list: list) -> dict:
    if len(key_list) != len(value_list):
        raise ValueError("Lists must be of the same length")

    dictionary = {}

    for i in range(len(key_list)):
        dictionary[key_list[i]] = value_list[i]

    return dictionary


def chunk_list(my_list: list, chunks: int) -> list:
    if len(my_list) == 0:
        raise ValueError("The list must not be empty")

    if len(my_list) % chunks != 0:
        raise ValueError("The list length must be divisible by chunk size")

    new_list = []
    for i in range(0, len(my_list), chunks):
        new_list.append(my_list[i:i + chunks])

    return new_list


class Book:
    def __init__(self, name: str, author: str, genre: str, borrowed: bool = False) -> None:
        self.name = name
        self.author = author
        self.genre = genre
        self.borrowed = borrowed

    def __str__(self) -> str:
        return f"{self.name}, {self.author}, " + (self.genre if self.borrowed else str(False))


class Library:
    def __init__(self):
        self.book_list = []

    def add_book(self, book: Book):
        if isinstance(book, Book):
            self.book_list.append(book)

    def get_all_books(self) -> list:
        return self.book_list

    def borrow_book(self, book: Book):
        for current_book in self.book_list:
            if current_book.name == book.name:
                if current_book.borrowed is True:
                    print("Book already borrowed")
                else:
                    current_book.borrowed = True

                return

        print("Book does not exist")

    def return_book(self, book: Book):
        for current_book in self.book_list:
            if current_book.name == book.name:
                if current_book.borrowed is False:
                    print("Book has not been borrowed")
                else:
                    current_book.borrowed = False

                return

        print("Book does not exist")


class BookStack:
    def __init__(self):
        self.stack = []

    def push(self, book):
        if isinstance(book, Book):
            self.stack.append(book)

    def pop(self) -> Book:
        if self.stack:
            return self.stack.pop(0)

    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def size(self) -> int:
        return len(self.stack)


def count_words(file_path: str) -> int:
    with open(file_path, "r") as my_file:
        return len(my_file.read().split())


def count_lines(file_path: str) -> int:
    with open(file_path, "r") as my_file:
        return len(my_file.readlines())


def write_even(input_file_path: str, output_file_path):
    with open(input_file_path, "r") as input_file:
        with open(output_file_path, "w") as output_file:
            for line in input_file.readlines()[1::2]:
                output_file.write(line)