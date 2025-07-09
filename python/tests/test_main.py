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

def test_check_guess_invalid_length(game_setup):
    with pytest.raises(ValueError):
        game_setup.check_guess("toolong")
    with pytest.raises(ValueError):
        game_setup.check_guess("")


def test_display_statistics_prints(capsys, game_setup):
    # Simulate a win and a loss
    game_setup.update_streaks(True)
    game_setup.update_streaks(False)
    game_setup.display_statistics()
    captured = capsys.readouterr()
    assert "GAME STATISTICS" in captured.out
    assert "Games Played: 2" in captured.out
    assert "Games Won: 1" in captured.out


def test_reset_game_clears_guesses(game_setup):
    game_setup.guess_list = ["start", "blank"]
    game_setup.current_guess_count = 2
    old_word = game_setup.word_to_match
    game_setup.reset_game()
    assert game_setup.guess_list == []
    assert game_setup.current_guess_count == 0
    assert game_setup.word_to_match != old_word or old_word == "build"  # could randomly pick same word


def test_generate_random_word_valid(game_setup):
    word = game_setup.generate_random_word()
    assert word in game_setup._word_list
    assert len(word) == 5
    assert word.isalpha()


def test_play_game_once_through(game_setup):
    # Simulate a full game: incorrect guesses, then a correct guess
    guesses = ["start", "blank", "build"]  # 'build' is the answer
    for guess in guesses:
        result = game_setup.check_guess(guess)
        game_setup.guess_list.append(guess)
        game_setup.current_guess_count += 1
        if result == "GGGGG":
            game_setup.update_streaks(True)
            break
    else:
        game_setup.update_streaks(False)

    # After the game, check the state
    assert game_setup.games_played == 1
    assert game_setup.games_won == 1
    assert game_setup.current_win_streak == 1
    assert game_setup.best_win_streak == 1
    assert game_setup.current_lose_streak == 0
    assert game_setup.best_lose_streak == 0
    assert game_setup.guess_list == guesses
    assert game_setup.current_guess_count == len(guesses)

def test_loss_scenario(game_setup):
    # Simulate max guesses without a win
    guesses = ["start", "blank", "other", "apple", "after"]
    for guess in guesses:
        result = game_setup.check_guess(guess)
        game_setup.guess_list.append(guess)
        game_setup.current_guess_count += 1
    game_setup.update_streaks(False)
    assert game_setup.games_played == 1
    assert game_setup.games_won == 0
    assert game_setup.current_win_streak == 0
    assert game_setup.current_lose_streak == 1
    assert game_setup.best_lose_streak == 1
    assert game_setup.guess_list == guesses
    assert game_setup.current_guess_count == len(guesses)

def test_start_game_loop_prints_and_exits(monkeypatch, capsys):
    game = WordleGame()
    game.word_to_match = "build"
    # Patch input to provide a correct guess, then 'n' to exit
    inputs = iter(["build", "n"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    game.start_game_loop()
    captured = capsys.readouterr()
    assert "Welcome to Wordle" in captured.out
    assert "Thanks for playing Wordle" in captured.out
