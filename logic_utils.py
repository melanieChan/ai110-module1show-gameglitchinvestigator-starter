def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty.

    Args:
        difficulty: One of "Easy", "Normal", or "Hard". Any other value
            falls back to the "Normal" range.

    Returns:
        A tuple (low, high) giving the inclusive bounds of the range.
    """
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Args:
        raw: The raw text entered by the user. May be None or empty,
            and may contain a decimal value (e.g. "5.0").

    Returns:
        A tuple (ok, guess_int, error_message):
            ok: True if parsing succeeded, False otherwise.
            guess_int: The parsed integer guess, or None on failure.
            error_message: A user-facing error string, or None on success.
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    Args:
        guess: The player's guess. Typically an int, but may be any
            type comparable to secret.
        secret: The target value the guess is being compared against.

    Returns:
        A tuple (outcome, message):
            outcome: One of "Win", "Too High", or "Too Low".
            message: A user-facing hint describing the outcome.
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret:
            # Fixed hint-direction bug by instructing agent to swap messages
            return "Too High", "📉 Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number.

    Args:
        current_score: The player's score before this update.
        outcome: The result of the guess, as returned by check_guess.
        attempt_number: The count of attempts made so far.

    Returns:
        The updated score.
    """
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        # Fixed score below 0 bug by telling agent to add clamp
        return max(0, current_score - 5)

    if outcome == "Too Low":
        # Fixed score below 0 bug by telling agent to add clamp
        return max(0, current_score - 5)

    return current_score
