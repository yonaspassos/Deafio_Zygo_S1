import json, sys


def read_file():
    with open("books.json", "r") as file:
        return json.load(file)

def get_book_title(book):
    return book["book_title"]

def get_author_book(author):
    return author["author"]

def get_year_book(year):
    return year["edition_year"]

def sort(sort_direction):
    if sort_direction is None:
        return "Ordering Exception"
    if len(sort_direction) == 0:
        return []
    books = read_file()
    if sort_direction.get("title"):
        books = sorted(books, key=get_book_title, reverse=(sort_direction["title"] == "desc"))
    if sort_direction.get("author"):
        books = sorted(books, key=get_author_book, reverse=(sort_direction["author"] == "desc"))
    if sort_direction.get("edition_year"):
        books = sorted(books, key=get_year_book, reverse=(sort_direction["edition_year"] == "desc"))
    return books


if __name__ == "__main__":
    params = None
    if len(sys.argv) >= 2:
        params = json.load(open(sys.argv[1]))
    print(sort(params))
