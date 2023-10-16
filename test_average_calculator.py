
import pytest
from average_calculator import AverageCalculator

# Создаем объект AverageCalculator
calculator = AverageCalculator()

def test_calculate_average_empty_list():
    assert calculator.calculate_average([]) == 0

def test_calculate_average_non_empty_list():
    assert calculator.calculate_average([1, 2, 3, 4, 5]) == 3.0

def test_compare_averages_first_list_bigger():
    assert calculator.compare_averages([1, 2, 3], [1, 2]) == "Первый список имеет большее среднее значение"

def test_compare_averages_second_list_bigger():
    assert calculator.compare_averages([1, 2], [1, 2, 3]) == "Второй список имеет большее среднее значение"

def test_compare_averages_equal():
    assert calculator.compare_averages([1, 2, 3], [1, 2, 3]) == "Средние значения равны"

