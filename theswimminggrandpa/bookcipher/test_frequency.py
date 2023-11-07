import pytest
from word_frequency import word_frequency, sort_by_frequency

def test_empty_file():
    assert word_frequency('empty.txt') == {}

def test_single_word():
    assert word_frequency('single_word.txt') == {'Python': 1}

def test_repeated_words():
    assert word_frequency('repeated_words.txt') == {'Python': 3}

def test_multiple_words():
    assert word_frequency('multiple_words.txt') == {'Python': 1, 'is': 1, 'great': 1}

def test_punctuation():
    assert word_frequency('punctuation.txt') == {'Python': 1, 'is': 1, 'great!': 1}

def test_large_file():
    frequency = word_frequency('large_file.txt')
    sorted_frequency = sort_by_frequency(frequency)
    # Check the first few words and their frequencies
    assert sorted_frequency[:3] == [('the', 1000), ('and', 500), ('a', 300)]