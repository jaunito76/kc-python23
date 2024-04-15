import word_frequency as wf

def test_empty_file():
    assert wf.word_frequency('empty.txt') == {}

def test_single_word():
    assert wf.word_frequency('single_word.txt') == {'python': 1}

def test_repeated_words():
    assert wf.word_frequency('repeated_words.txt') == {'python': 3}

def test_multiple_words():
    assert wf.word_frequency('multiple_words.txt') == {'python': 1, 'is': 1, 'great': 1}

def test_punctuation():
    assert wf.word_frequency('punctuation.txt') == {'python': 1, 'is': 1, 'great': 1}

def test_large_file():
    frequency = wf.word_frequency('large_file.txt')
    assert frequency == {'the':1000, 'and':500, 'a':300}
    
def test_sorted():
    frequency = wf.word_frequency('large_file.txt')
    sorted_frequency = wf.sort_by_frequency(frequency)
    # Check the first few words and their frequencies
    assert sorted_frequency[:3] == [('the', 1000), ('and', 500), ('a', 300)]