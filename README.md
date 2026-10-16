
# qa_python

## Проект 4-го спринта Яндекс Практикума

Автоматизированные тесты для класса BooksCollector.

Класс позволяет добавлять книги, назначать им жанры, получать списки книг по жанрам и возрастным ограничениям, а также управлять избранным.

## Реализованные тесты

1. test_add_new_book_adds_two_books — добавление двух книг.
2. test_add_new_book_invalid_name_not_added — проверка недопустимой длины названия книги.
3. test_set_book_genre_sets_genre — установка жанра книги.
4. test_get_book_genre_returns_genre — получение жанра книги.
5. test_get_books_with_specific_genre_returns_books — получение книг определённого жанра.
6. test_get_books_genre_returns_dictionary — получение словаря книг и жанров.
7. test_get_books_for_children_excludes_adult_genres — исключение книг с возрастными ограничениями.
8. test_add_book_in_favorites_adds_book_once — добавление книги в избранное без дублирования.
9. test_delete_book_from_favorites_deletes_book — удаление книги из избранного.
10. test_get_list_of_favorites_books_returns_books — получение списка избранных книг.

Для проверки граничных значений и возрастных ограничений используется параметризация pytest.

## Запуск тестов

Установить pytest:

```bash
python -m pip install pytest
```

Запустить тесты:

```bash
python -m pytest -v tests.py
```

Результат проверки: 12 passed.
