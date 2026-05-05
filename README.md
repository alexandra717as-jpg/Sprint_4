# Проект: Тестирование приложения BooksCollector

В рамках данного проекта реализованы автотесты для проверки функциональности приложения по управлению списком книг и их жанрами.

## Список реализованных тестов:
1. `test_add_new_book_add_two_books` — проверка добавления двух разных книг.
2. `test_add_new_book_double_add_not_possible` — проверка невозможности добавления дубликата книги.
3. `test_set_book_genre_valid_genre` — проверка установки жанра для существующей книги.
4. `test_get_books_with_specific_genre_get_horror` — проверка получения списка книг по конкретному жанру.
5. `test_get_books_for_children_allowed_genres` — проверка доступности детских жанров.
6. `test_get_books_for_children_horror_not_allowed` — проверка отсутствия книг с возрастным рейтингом в детском списке.
7. `test_add_book_in_favorites_added_successfully` — проверка добавления книги в избранное.
8. `test_delete_book_from_favorites_deleted_successfully` — проверка удаления книги из избранного.
9. `test_add_book_in_favorites_not_in_list_not_added` — проверка, что нельзя добавить в избранное несуществующую книгу.
10. `test_set_genre_for_different_books` (параметризация) — проверка установки жанров "Ужасы", "Детективы" и "Мультфильмы".

## Запуск тестов:
```bash
pytest -v test_books_collector.py
```