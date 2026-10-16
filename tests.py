
import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_adds_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Шерлок Холмс')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('name', ['', 'А' * 41])
    def test_add_new_book_invalid_name_not_added(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name not in collector.get_books_genre()

    def test_set_book_genre_sets_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert collector.get_books_genre()['Гарри Поттер'] == 'Фантастика'

    def test_get_book_genre_returns_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        assert collector.get_book_genre('Шерлок Холмс') == 'Детективы'

    def test_get_books_with_specific_genre_returns_books(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.set_book_genre('Книга 1', 'Комедии')
        collector.set_book_genre('Книга 2', 'Ужасы')
        assert collector.get_books_with_specific_genre('Комедии') == ['Книга 1']

    def test_get_books_genre_returns_dictionary(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        assert collector.get_books_genre() == {'Гарри Поттер': ''}

    @pytest.mark.parametrize('genre', ['Ужасы', 'Детективы'])
    def test_get_books_for_children_excludes_adult_genres(self, genre):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', genre)
        assert collector.get_books_for_children() == []

    def test_add_book_in_favorites_adds_book_once(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        assert collector.get_list_of_favorites_books() == ['Гарри Поттер']

    def test_delete_book_from_favorites_deletes_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.delete_book_from_favorites('Гарри Поттер')
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_returns_books(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.add_book_in_favorites('Книга 1')
        collector.add_book_in_favorites('Книга 2')
        assert collector.get_list_of_favorites_books() == ['Книга 1', 'Книга 2']

