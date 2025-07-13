import pytest
from string_utils import StringUtils

string_utils = StringUtils()

# ===== Тесты для capitalize =====
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("a", "A"),  # Граничный случай: одна буква
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),  # Число в начале
    ("", ""),              # Пустая строка
    ("   ", "   "),        # Только пробелы
    ("Skypro", "Skypro"),  # Уже заглавная первая буква
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

# ===== Тесты для trim =====
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("  hello", "hello"),
    ("\tsome text", "\tsome text"),  # Не удаляет табуляцию
    ("no_spaces", "no_spaces"),      # Нет пробелов
    (" ", ""),                       # Один пробел
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("   ", ""),                     # Только пробелы
    ("skypro   ", "skypro   "),       # Пробелы в конце
    ("  a  ", "a  "),                # Пробелы внутри
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

# ===== Тесты для contains =====
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "k", True),
    ("SkyPro", "o", True),
    ("123", "2", True),
    ("", "", True),  # Спорный случай
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "U", False),
    ("", "a", False),      # Пустая строка
    ("Hello", "h", False), # Регистрозависимость
    ("123", "4", False),
])
def test_contains_negative(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected

# ===== Тесты для delete_symbol =====
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("aaaa", "a", ""),     # Удаление всех символов
    ("a1b2c3", "2", "a1bc3"),
    ("", "a", ""),         # Пустая строка
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "X", "SkyPro"),  # Символ отсутствует
    ("Hello", "h", "Hello"),    # Регистрозависимость
    ("   ", " ", ""),           # Удаление всех пробелов
])
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected
