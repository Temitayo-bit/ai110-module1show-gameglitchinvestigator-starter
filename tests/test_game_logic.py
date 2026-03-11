from logic_utils import check_guess, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# Fix 1: out-of-range guesses should be rejected, not accepted
def test_parse_guess_rejects_negative_number():
    # A negative number like -5 is out of range and must not be accepted
    ok, value, error = parse_guess("-5")
    assert ok is False, "Negative numbers should be rejected"
    assert value is None
    assert error is not None

def test_parse_guess_rejects_zero():
    # Zero is below the valid range (1–100) and must be rejected
    ok, value, error = parse_guess("0")
    assert ok is False, "Zero should be rejected"
    assert value is None
    assert error is not None

def test_parse_guess_rejects_above_100():
    # Numbers above 100 are out of range and must not be accepted
    ok, value, error = parse_guess("150")
    assert ok is False, "Numbers above 100 should be rejected"
    assert value is None
    assert error is not None


# Fix 2: hints must reflect the correct direction
def test_hint_says_go_higher_when_guess_is_below_secret():
    # Guess (30) is below secret (70) — hint must say Go HIGHER, not Go LOWER
    outcome, message = check_guess(30, 70)
    assert outcome == "Too Low"
    assert "HIGHER" in message.upper(), f"Expected 'HIGHER' in hint, got: {message}"

def test_hint_says_go_lower_when_guess_is_above_secret():
    # Guess (80) is above secret (40) — hint must say Go LOWER, not Go HIGHER
    outcome, message = check_guess(80, 40)
    assert outcome == "Too High"
    assert "LOWER" in message.upper(), f"Expected 'LOWER' in hint, got: {message}"
