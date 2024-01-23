import os
import random
import csv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql://postgres:123456@localhost:5432/web1")
db = scoped_session(sessionmaker(bind=engine))

def main():
    weights = [5, 10, 20, 60, 5]
    numbers = [1, 2, 3, 4, 5]
    for i in range(5, 10):
        for j in range(3, 5003):
            user_id = i
            book_id = j
            rating = random.choices(numbers, weights=weights, k=1)[0]
            if rating == 1:
                comment = "I hate this book"
            elif rating == 2:
                comment = "I don't like this book"
            elif rating == 3:
                comment = "This book is ok"
            elif rating == 4:
                comment = "I like this book"
            else:
                comment = "I love this book"

            db.execute(text("INSERT INTO reviews (user_id, book_id, rating, comment) VALUES (:user_id, :book_id, :rating, :comment)"),
               {"user_id": user_id, "book_id": book_id, "rating": rating, "comment": comment})
            db.commit()

if __name__ == "__main__":
    main()