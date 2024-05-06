from flask import Flask, render_template, request
from sqlalchemy.orm import sessionmaker

from model import Book_Details, engine

app = Flask(__name__)

Session = sessionmaker(bind=engine)
session = Session()

book_details = Book_Details()

books = []

@app.route('/', methods=["GET","POST"])
def home():
    book = session.query(Book_Details).all()

    for i in range(len(book)):
        book_information = {
            "book_name": book[i].book_name,
            "author": book[i].author,
            "rating": book[i].rating
        }

        books.append(book_information)
        print(books)

    return render_template("index.html", book_list = books)

@app.route("/add", methods=["POST", "GET"])
def add():

    if request.method == "POST":
        book_details.book_name = request.form.get("book_name")
        book_details.author = request.form.get("author")
        book_details.rating = request.form.get("rating")

        session.add(book_details)
        session.commit()

    return render_template("add.html")

if __name__ == "__main__":
    app.run(debug=True)

