import pytest
from py_check.main import WordleGame

@pytest.fixture
def game_setup():
    # Reset the game state before each test
    game = WordleGame()
    game.word_to_match = "build"
    return game

def test_get_word_to_match(game_setup):
    assert game_setup.get_word_to_match() == "build"

def test_get_guess_list(game_setup):
    assert game_setup.get_guess_list() == []

def test_check_guess_fail(game_setup):
    result = game_setup.check_guess("start")
    assert result == "-----"

def test_check_guess_part_fail(game_setup):
    result = game_setup.check_guess("blank")
    assert result == "GY---"

def test_check_guess_part_fail_dup_letters(game_setup):
    result = game_setup.check_guess("balls")
    assert result == "G--G-"

def test_check_guess_part_fail_dup_letters_two(game_setup):
    result = game_setup.check_guess("allee")
    assert result == "--Y--"

def test_check_guess_part_fail_dup_letters_three(game_setup):
    game_setup.word_to_match = "after"
    result = game_setup.check_guess("fluff")
    assert result == "----Y"

def test_check_guess_part_fail_dup_letters_four(game_setup):
    game_setup.word_to_match = "fluff"
    result = game_setup.check_guess("after")
    assert result == "-Y---"

def test_check_guess_part_fail_dup_letters_five(game_setup):
    game_setup.word_to_match = "affix"
    result = game_setup.check_guess("fluff")
    assert result == "---YY"

def test_check_guess_pass(game_setup):
    result = game_setup.check_guess("build")
    assert result == "GGGGG"

def test_generate_random_word(game_setup):
    result = game_setup.generate_random_word()
    assert len(result) == 5
    assert result.isalpha()

def test_reset_game(game_setup):
    org_word = game_setup.get_word_to_match()
    game_setup.reset_game()
    assert game_setup.get_word_to_match() != org_word

def test_update_streaks(game_setup):
    game_setup.update_streaks(True)
    assert game_setup.games_played == 1
    assert game_setup.games_won == 1
    assert game_setup.current_win_streak == 1
    assert game_setup.best_win_streak == 1

    game_setup.update_streaks(False)
    assert game_setup.games_played == 2
    assert game_setup.games_won == 1
    assert game_setup.current_win_streak == 0
    assert game_setup.current_lose_streak == 1
    assert game_setup.best_lose_streak == 1
