import os
import csv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql://postgres:123456@localhost:5432/web1")
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("users.csv")  # replace with your csv file name
    reader = csv.reader(f)
    next(reader)  # Skip the header row.
    for firstName, lastName, email, password in reader:
        db.execute(text("INSERT INTO users (firstName, lastName, email, password) VALUES (:firstName, :lastName, :email, :password)"),
                   {"firstName": firstName, "lastName": lastName, "email": email, "password": password})
    db.commit()

if __name__ == "__main__":
    main()