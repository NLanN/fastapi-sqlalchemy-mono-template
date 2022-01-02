from typing import Generator

from src.db.session import SessionLocal


def get_session() -> Generator:
    try:
        session = SessionLocal()
        yield session
    finally:
        session.close()
