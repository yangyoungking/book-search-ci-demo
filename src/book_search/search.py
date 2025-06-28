def search_books(
    query, books, author=None, match_mode="exact", limit=None
):
    """图书搜索：支持模糊匹配、作者过滤、结果限制"""
    result = []
    q = query.lower().strip()

    for book in books:
        title = book.get("title", "").lower()
        book_author = book.get("author", "").lower()

        if match_mode == "exact" and q != title:
            continue
        elif match_mode == "fuzzy" and q not in title:
            continue
        elif match_mode not in ("exact", "fuzzy"):
            raise ValueError("Invalid match_mode. Use 'exact' or 'fuzzy'.")

        if author and author.lower() not in book_author:
            continue

        result.append(book)
        if limit and len(result) >= limit:
            break

    return result
