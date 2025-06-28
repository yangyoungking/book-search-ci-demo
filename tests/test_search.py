import pytest
from book_search import search_books

books = [
    {"title": "Python Programming", "author": "John Doe"},
    {"title": "Data Structures", "author": "Jane Smith"},
    {"title": "Advanced Python", "author": "John Doe"},
    {"title": "Machine Learning", "author": "Alan Turing"}
]

@pytest.mark.parametrize("query,mode,expected_count", [
    ("Data Structures", "exact", 1),
    ("Python", "fuzzy", 2),
    ("Machine", "fuzzy", 1),
    ("Unknown", "fuzzy", 0)
])
def test_query_matching(query, mode, expected_count):
    result = search_books(query, books, match_mode=mode)
    assert len(result) == expected_count

def test_author_filter():
    result = search_books("Python", books, match_mode="fuzzy", author="john")
    assert len(result) == 2

def test_limit():
    result = search_books("Python", books, match_mode="fuzzy", limit=1)
    assert len(result) == 1

def test_invalid_match_mode():
    with pytest.raises(ValueError):
        search_books("Python", books, match_mode="partial")
