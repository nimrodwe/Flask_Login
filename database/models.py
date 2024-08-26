from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import mapped_column, relationship
from app import db
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime



class User(db.model):

    __tablename__ = "users"

    id = mapped_column(Integer(), primary_key=True, autoincrement=True)
    email = mapped_column(String(), nullable=False, unique=True)
    password_hashed = mapped_column(String(), nullable=False, unique=True)
    registered_on = mapped_column(DateTime(), nullable=False)

    def __init__(self, email: str, password_text: str):
        self.email = email
        self.password = self._generate_password(password_text)
        self.registered_on = datetime.now()

    user_relationship = relationship("Book", back_populates="")

    def is_password_correct(self, password_text):
        return check_password_hash(self.password, password_text)
    
    def set_password(self, password_text):
        self.password = self._generate_password(password_text)

    @staticmethod
    def _generate_password(password_text):
        return generate_password_hash(password_text)
    
    def __repr__(self):
        return f"<User {self.email}>"
    
class Book(db.Model):

    __tablename__ = "books"

    id = mapped_column(Integer(), primary_key=True, autoincrement=True)
    title = mapped_column(String(), nullable=False)
    author = mapped_column(String())
    rating = mapped_column(Integer(), nullable=False)
    user_id = mapped_column(ForeignKey("users.id"))
    
    books_relationship = relationship("User", back_populates="books")

    def __init__(self, book_title: str, book_author: str, book_rating: int, user_id: int):
        self.title = book_title
        self.author = book_author
        self.rating = book_rating
        self.user_id = user_id
    
    def __repr__(self):
        return f"<Book {self.title}>"
