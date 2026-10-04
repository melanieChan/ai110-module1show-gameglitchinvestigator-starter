from logic_utils import check_guess, update_score, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

def test_hint_message_direction():
    # A guess that is too high must tell the player to go LOWER, and a
    # guess that is too low must tell the player to go HIGHER.
    _, too_high_message = check_guess(60, 50)
    assert "LOWER" in too_high_message

    _, too_low_message = check_guess(40, 50)
    assert "HIGHER" in too_low_message

def test_score_does_not_go_negative_on_too_low():
    # Score should clamp at 0 instead of going negative on a "Too Low" guess.
    new_score = update_score(current_score=0, outcome="Too Low", attempt_number=1)
    assert new_score == 0

def test_score_does_not_go_negative_on_too_high_odd_attempt():
    # "Too High" subtracts points but should still clamp at 0.
    new_score = update_score(current_score=0, outcome="Too High", attempt_number=1)
    assert new_score == 0

def test_parse_guess_within_range_is_accepted():
    # Guesses inside the low/high bounds, including the boundaries
    # themselves, should all parse successfully.
    for raw, expected in [("1", 1), ("50", 50), ("100", 100)]:
        ok, guess_int, err = parse_guess(raw, low=1, high=100)
        assert ok is True
        assert guess_int == expected
        assert err is None

def test_parse_guess_above_range_is_rejected():
    # A guess above the high bound should be rejected with an error message.
    ok, guess_int, err = parse_guess("150", low=1, high=100)
    assert ok is False
    assert guess_int is None
    assert err == "Enter a number between 1 and 100."

def test_parse_guess_below_range_is_rejected():
    # A guess below the low bound should be rejected with an error message.
    ok, guess_int, err = parse_guess("0", low=1, high=100)
    assert ok is False
    assert guess_int is None
    assert err == "Enter a number between 1 and 100."

def test_parse_guess_non_numeric_is_rejected():
    # Non-numeric input should fail before range checking even applies.
    ok, guess_int, err = parse_guess("abc", low=1, high=100)
    assert ok is False
    assert guess_int is None
    assert err == "That is not a number."

def test_parse_guess_empty_input_is_rejected():
    # Empty input should prompt the user to enter a guess.
    ok, guess_int, err = parse_guess("", low=1, high=100)
    assert ok is False
    assert guess_int is None
    assert err == "Enter a guess."
