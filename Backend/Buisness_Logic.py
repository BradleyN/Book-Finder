from Backend.BooksTable import BooksTable

#Get the book data without using and filtering.
def get_books_unfiltered():
    return BooksTable().fetch_books(limit=100)

#Get the full information for a particular book
def fetch_book_info(book):
    #Get the id of the currently selected book
    book_id = book["book_id"]
    #get the info associated with that book. fetch_book_info returns a list so grab the first item in that list
    extra_info = BooksTable().fetch_book_info(id_filter=book_id)[0]
    #Add data from extra_info to book. Basically we're just combining the dictionaries here
    extra_info.update(book)
    return extra_info

def apply_filters(genre_filter, year_input):
    if genre_filter == "":
        genre_filter = None
    else:
        #TODO: Find a better solution for this
        genre_filter = genre_filter.capitalize()

    try:
        #Try casting to an int to see if it is a valid integer.
        year_filter = str(int(year_input))
    except ValueError:
        print("That is not a valid year")
        year_filter = None

    print(f"Filtering by Genre: {genre_filter}, year: {year_filter}")

    #REFACTOR?
    if genre_filter is None and year_filter is None:
        books = get_books_unfiltered()
    else:
        books_with_year = BooksTable().fetch_books_with_year(year_filter,limit=20)
        print(books_with_year)
        books = []
        for book_info in books_with_year:
            book = BooksTable().fetch_books(id_filter=book_info["id"])[0]
            books.append(book)
    return books