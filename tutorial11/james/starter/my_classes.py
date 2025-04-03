import csv

# Practice Problem: OOP + CSV
class SensorReader:
    def __init__(self, filename):
        """
        Initializes the SensorReader with a given CSV filename.
        """
        # TODO

    def read_data(self):
        """
        Reads the CSV file and stores all rows in self.data.
        """
        # TODO
       

    def __str__(self):
        """
        Returns a string with basic information:
        - The filename
        - How many rows of data have been loaded
        """
        # TODO
       

    def save_filtered_data(self, output_file, threshold):
        """
        Saves only the rows where 'voltage' (assumed to be in column index 1)
        is above the specified threshold.

        Writes the filtered data to the specified output file.
        """
        # TODO
       


# Practice Problem: OOP + File I/O
class Book:
    def __init__(self, title, author, year, is_checked_out=False):
        self.title = title
        self.author = author
        self.year = year
        self.is_checked_out = is_checked_out # default value is False

    def check_out(self):
        self.is_checked_out = True

    def return_book(self):
        self.is_checked_out = False

    def __str__(self):
        status = "[Checked Out]" if self.is_checked_out else "[Available]"
        return status + " " + self.title + " by " + self.author + " (" + str(self.year) + ")"

class Library:
    def __init__(self):
        self.books = []  # will hold a list of Book objects

    def load_books_from_csv(self, filename):
        """
        Reads a CSV where each row contains: title,author,year
        (Optional) We can also handle book status if the CSV has 4 columns:
        title,author,year,is_checked_out
        """
        self.books = []  # clear existing list before loading
        with open(filename, mode='r', newline='') as csvfile:
            # TODO

    def save_books_to_csv(self, filename):
        """
        Writes the same format to CSV, including the current status.
        For each book, we write: title,author,year,is_checked_out
        """
        with open(filename, mode='w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            for book in self.books:
                csv_writer.writerow([
                    # TODO 
                    # # Convert is_checked_out to a string (True/False)
                ])

    def find_book_by_title(self, title):
        """
        Returns the Book object if a matching title is found, otherwise None.
        """
        # TODO
        return None

    def check_out_book(self, title):
        """
        If found and available, mark the book as checked out.
        If not found, or already checked out, handle gracefully.
        """
        book = self.find_book_by_title(title)
        if book is None:
            print("Could not find a book with title:", title)
        else:
            # TODO
