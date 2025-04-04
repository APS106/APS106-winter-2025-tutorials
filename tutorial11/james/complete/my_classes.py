import csv

# Practice Problem: OOP + CSV
class SensorReader:
    def __init__(self, filename):
        """
        Initializes the SensorReader with a given CSV filename.
        """
        self.filename = filename
        self.data = []  # will store the CSV data after read_data() is called

    def read_data(self):
        """
        Reads the CSV file and stores all rows in self.data.
        """
        with open(self.filename, mode='r', newline='') as file: # open the file in read mode with newline '' to avoid issues with csv module
            csv_reader = csv.reader(file)
            # Read every row (including header) and append to self.data
            for row in csv_reader:
                self.data.append(row)

    def __str__(self):
        """
        Returns a string with basic information:
        - The filename
        - How many rows of data have been loaded
        """
        row_count = len(self.data)
        return "SensorReader reading from " + self.filename + ": " + str(row_count) + " rows loaded."

    def save_filtered_data(self, output_file, threshold):
        """
        Saves only the rows where 'voltage' (assumed to be in column index 1)
        is above the specified threshold.

        Writes the filtered data to the specified output file.
        """
        if not self.data:
            # If data is empty, there's nothing to filter or write
            return

        with open(output_file, mode='w', newline='') as f_out: # open the file in write mode with newline '' to avoid issues with csv module
            csv_writer = csv.writer(f_out)

            # Write the header row (assuming the first row in self.data is the header)
            csv_writer.writerow(self.data[0])

            # Write only rows with voltage > threshold
            for row in self.data[1:]:
                # Assuming column index 1 is "voltage"
                voltage_value = float(row[1])
                if voltage_value > threshold:
                    csv_writer.writerow(row)


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
        if self.is_checked_out:
            status = "[Checked Out]"
        else: 
            status = "[Available]"
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
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                # If there's a column for is_checked_out:
                # title, author, year, is_checked_out
                if len(row) == 4:
                    title, author, year, checked_out_str = row
                    is_checked_out = (checked_out_str.lower() == "true")
                else:
                    # otherwise assume it's just three columns
                    title, author, year = row
                    is_checked_out = False
                book = Book(title, author, year, is_checked_out)
                self.books.append(book)

    def save_books_to_csv(self, filename):
        """
        Writes the same format to CSV, including the current status.
        For each book, we write: title,author,year,is_checked_out
        """
        with open(filename, mode='w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            for book in self.books:
                csv_writer.writerow([
                    book.title,
                    book.author,
                    book.year,
                    str(book.is_checked_out) # Convert is_checked_out to a string (True/False)
                ])

    def find_book_by_title(self, title):
        """
        Returns the Book object if a matching title is found, otherwise None.
        """
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
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
            if book.is_checked_out:
                print("Sorry, that book is already checked out.")
            else:
                book.check_out()
                print("You have successfully checked out:", book.title)
