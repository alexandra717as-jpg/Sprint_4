import pytest

class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_double_add_not_possible(self, collector):
        collector.add_new_book('Дюна')
        collector.add_new_book('Дюна')
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_valid_genre(self, collector):
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.get_book_genre('Оно') == 'Ужасы'

    def test_get_books_with_specific_genre_get_horror(self, collector):
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert 'Оно' in collector.get_books_with_specific_genre('Ужасы')

    def test_get_books_for_children_allowed_genres(self, collector):
        collector.add_new_book('Золушка')
        collector.set_book_genre('Золушка', 'Мультфильмы')
        assert 'Золушка' in collector.get_books_for_children()

    def test_get_books_for_children_horror_not_allowed(self, collector):
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        assert 'Сияние' not in collector.get_books_for_children()

    def test_add_book_in_favorites_added_successfully(self, collector):
        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')
        assert '1984' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_deleted_successfully(self, collector):
        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')
        collector.delete_book_from_favorites('1984')
        assert '1984' not in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_not_in_list_not_added(self, collector):
        collector.add_book_in_favorites('Несуществующая книга')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_get_books_genre_returns_dict(self, collector):
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.get_books_genre() == {'Оно': 'Ужасы'}

    def test_get_book_genre_by_name(self, collector):
        collector.add_new_book('Шерлок')
        collector.set_book_genre('Шерлок', 'Детективы')
        assert collector.get_book_genre('Шерлок') == 'Детективы'

    @pytest.mark.parametrize('name', [
        'А',  
        'А' * 40  
    ])
    def test_add_new_book_valid_length_added(self, collector, name):
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('name', [
        '',  
        'А' * 41  
    ])
    def test_add_new_book_invalid_length_not_added(self, collector, name):
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 0
        