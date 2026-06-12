from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()

class Book(BaseModel):
    title: str = Field(..., min_length=1)
    author: str = Field(..., min_length=1)
    year: int = Field(..., gt=0, description="Year the book was published")

class BookIn(Book):
    pass

class BookOut(Book):
    id: int

books = [
    {"id": 1, "title": "1984", "author": "George Orwell", "year": 1949},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
]

@app.get("/books", response_model=List[BookOut])
def list_books():
    return books

@app.get("/books/{book_id}", response_model=BookOut)
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.post("/books", response_model=BookOut, status_code=201)
def create_book(book: BookIn):
    new_id = max(book_item["id"] for book_item in books) + 1 if books else 1
    new_book = {"id": new_id, **book.dict()}
    books.append(new_book)
    return new_book

@app.put("/books/{book_id}", response_model=BookOut)
def update_book(book_id: int, book: BookIn):
    for index, existing_book in enumerate(books):
        if existing_book["id"] == book_id:
            updated_book = {"id": book_id, **book.dict()}
            books[index] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int):
    for index, existing_book in enumerate(books):
        if existing_book["id"] == book_id:
            books.pop(index)
            return
    raise HTTPException(status_code=404, detail="Book not found")

# Example requests:
# GET /books
# GET /books/1
# POST /books with JSON body {"title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937}
# PUT /books/2 with JSON body {"title": "New Title", "author": "Author Name", "year": 2024}
# DELETE /books/1
