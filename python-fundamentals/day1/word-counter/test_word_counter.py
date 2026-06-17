# test_word_counter.py
from v2_idiomatic import count_words

def test_counts_repeated_word():
    result = count_words("cat dog cat")
    # cat appears twice, dog once → top entry should be ("cat", 2)
    assert result[0] == ("cat", 2)

def test_lowercases():
    result = count_words("The the")
    assert result[0] == ("the", 2)

def test_strips_punctuation():
    result = count_words("hi, hi.")
    # punctuation gone → ("hi", 2)
    assert result[0] == ("hi", 2)

def test_returns_at_most_5():
    result = count_words("a b c d e f g")   # 7 distinct words
    assert len(result) == 5 

def test_returns_at_most_3():
    result = count_words("a b c d e f g", 3)   # 7 distinct words
    assert len(result) == 3

def test_empty_text():
    result = count_words("")
    assert result == []