import os
import csv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql://postgres:123456@localhost:5432/web1")
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("books.csv")  # replace with your csv file name
    reader = csv.reader(f)
    next(reader)  # Skip the header row.
    for isbn, title, author, year in reader:
        db.execute(text("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)"),
                   {"isbn": isbn, "title": title, "author": author, "year": int(year)})
    db.commit()

if __name__ == "__main__":
    main()