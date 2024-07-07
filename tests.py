import pytest
from main import BooksCollector
class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize("book_name", [
        'Очень сильно длинное название,должно быть больше 40 символов',
        ''
    ])
    def test_add_new_book_invalid_name(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 0
    @pytest.mark.parametrize("book_name, expected_genre", [
        ('Книга без жанра 1', ''),
        ('Книга без жанра 2', '')
    ])
    def test_add_new_book_without_genre(self, book_name, expected_genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert collector.get_book_genre(book_name) == expected_genre

    @pytest.mark.parametrize("book_name, genre, expected_genre", [
        ('Книга 1', 'Фантастика', 'Фантастика'),
        ('Книга 2', 'Ужасы', 'Ужасы'),
    ])
    def test_set_book_genre(self, book_name, genre, expected_genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == expected_genre

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.set_book_genre('Книга 1', 'Фантастика')
        collector.set_book_genre('Книга 2', 'Ужасы')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Книга 1']
        assert collector.get_books_with_specific_genre('Ужасы') == ['Книга 2']

    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.set_book_genre('Книга 1', 'Фантастика')
        expected_books_genre = {'Книга 1': 'Фантастика'}
        assert collector.get_books_genre() == expected_books_genre

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Детская книга')
        collector.set_book_genre('Детская книга', 'Мультфильмы')
        collector.add_new_book('Взрослая книга')
        collector.set_book_genre('Взрослая книга', 'Ужасы')
        collector.add_new_book('Взрослая книга1')
        collector.set_book_genre('Взрослая книга1', 'Детективы')
        assert collector.get_books_for_children() == ['Детская книга']

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Книга для избранного')
        collector.add_book_in_favorites('Книга для избранного')
        assert collector.get_list_of_favorites_books() == ['Книга для избранного']

    def test_add_book_in_favorites_not_in_books_genre(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Книга не из словаря')
        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Книга для удаления')
        collector.add_book_in_favorites('Книга для удаления')
        collector.delete_book_from_favorites('Книга для удаления')
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.add_book_in_favorites('Книга 1')
        collector.add_book_in_favorites('Книга 2')
        assert collector.get_list_of_favorites_books() == ['Книга 1', 'Книга 2']
