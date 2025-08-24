from typing import Optional, List
from uuid import uuid4

from sqlalchemy import String, ForeignKey, Column, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship, declarative_base
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy


Base = declarative_base()
db = SQLAlchemy(model_class=Base, engine_options=dict(echo=True))


class Contact(db.Model):
    __tablename__ = "contacts"

    id: Mapped[str] = mapped_column(String(100), primary_key=True)
    first_name: Mapped[str] = mapped_column(String(20))
    last_name: Mapped[str] = mapped_column(String(20))
    phone_number: Mapped[str] = mapped_column(String(15))
    bio: Mapped[Optional[str]] = mapped_column(String(), nullable=True, default=None)
    city: Mapped[Optional[str]] = mapped_column(String(20), nullable=True, default=None)
    user_id:Mapped[str] = mapped_column(ForeignKey("users.id"), primary_key=True)
    img: Mapped[Optional[str]] = mapped_column(String(), nullable=True, default=None)

    def __init__(self, *args, **kwargs):
        self.id = uuid4().hex
        super().__init__(*args, **kwargs)


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String(100), primary_key=True)
    username: Mapped[str] = mapped_column(String(20), unique=True)
    password_: Mapped[str] = mapped_column(String(500))
    fullname: Mapped[Optional[str]] = mapped_column(String(20), nullable=True, default=None)
    phone_number: Mapped[Optional[str]] = mapped_column(String(15), nullable=True, default=None)
    is_active:Mapped[bool] = mapped_column(Boolean(), default=True)
    contacts: Mapped[List[Contact]] = relationship()

    def __init__(self, *args, **kwargs):
        self.id = uuid4().hex
        super().__init__(*args, **kwargs)

    @property
    def password(self):
        return self.password_

    @password.setter
    def password(self, pwd):
        self.password_ = generate_password_hash(pwd)

    def is_verify_password(self, pwd) -> bool:
        return check_password_hash(self.password_, pwd)
