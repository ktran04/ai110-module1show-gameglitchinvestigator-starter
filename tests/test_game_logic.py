"""Pytest cases covering each bug fixed in the Game Glitch Investigator.

Each test class maps to one bug that was present in the original AI-generated
code and corrected in logic_utils.py.
"""

from logic_utils import (
    WRONG_GUESS_PENALTY,
    check_guess,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)


# Bug 1: Backwards hints.
# Original: a guess that was too high told the player to "Go HIGHER" and a
# guess that was too low told them to "Go LOWER". The direction was inverted.
class TestBackwardsHints:
    def test_win_returns_win_outcome_and_message(self):
        outcome, message = check_guess(50, 50)
        assert outcome == "Win"
        assert message == "🎉 Correct!"

    def test_too_high_tells_player_to_go_lower(self):
        outcome, message = check_guess(60, 50)
        assert outcome == "Too High"
        assert "LOWER" in message

    def test_too_low_tells_player_to_go_higher(self):
        outcome, message = check_guess(40, 50)
        assert outcome == "Too Low"
        assert "HIGHER" in message


# Bug 2: Difficulty ranges were swapped so Normal (1-100) was wider than
# Hard (1-50). Harder difficulty should mean a wider range.
class TestDifficultyRanges:
    def test_easy_range(self):
        assert get_range_for_difficulty("Easy") == (1, 20)

    def test_normal_range(self):
        assert get_range_for_difficulty("Normal") == (1, 50)

    def test_hard_range(self):
        assert get_range_for_difficulty("Hard") == (1, 100)

    def test_harder_difficulty_is_wider(self):
        _, easy_high = get_range_for_difficulty("Easy")
        _, normal_high = get_range_for_difficulty("Normal")
        _, hard_high = get_range_for_difficulty("Hard")
        assert easy_high < normal_high < hard_high

    def test_unknown_difficulty_defaults_to_normal_range(self):
        assert get_range_for_difficulty("???") == (1, 50)


# Bug 3: Win scoring off-by-one. Original used 100 - 10 * (attempt + 1), so a
# first-attempt win scored 80 instead of 100. Fixed to 100 - 10 * (attempt - 1).
class TestWinScoring:
    def test_first_attempt_win_scores_full_100(self):
        assert update_score(0, "Win", attempt_number=1) == 100

    def test_score_shrinks_by_10_per_attempt(self):
        assert update_score(0, "Win", attempt_number=2) == 90
        assert update_score(0, "Win", attempt_number=3) == 80

    def test_win_points_floor_at_10(self):
        # 100 - 10 * (10 - 1) = 10, and it should never drop below 10.
        assert update_score(0, "Win", attempt_number=10) == 10
        assert update_score(0, "Win", attempt_number=20) == 10

    def test_win_adds_to_existing_score(self):
        assert update_score(55, "Win", attempt_number=1) == 155


# Bug 4: Wrong-guess penalty glitch. Original gave +5 for a "Too High" guess on
# even attempts and let the score go negative. Every wrong guess should deduct a
# fixed penalty and the score should never fall below 0.
class TestWrongGuessPenalty:
    def test_too_high_deducts_penalty(self):
        assert update_score(20, "Too High", attempt_number=2) == 20 - WRONG_GUESS_PENALTY

    def test_too_high_on_even_attempt_still_deducts(self):
        # The old bug rewarded +5 on even attempts; confirm it now deducts.
        assert update_score(20, "Too High", attempt_number=4) == 15

    def test_too_low_deducts_penalty(self):
        assert update_score(20, "Too Low", attempt_number=1) == 15

    def test_score_never_drops_below_zero(self):
        assert update_score(3, "Too Low", attempt_number=1) == 0
        assert update_score(0, "Too High", attempt_number=1) == 0


# parse_guess was refactored out of app.py; these guard its contract so the
# refactor didn't introduce a regression.
class TestParseGuess:
    def test_empty_input_is_rejected(self):
        ok, value, err = parse_guess("")
        assert ok is False
        assert value is None
        assert err == "Enter a guess."

    def test_none_input_is_rejected(self):
        ok, value, err = parse_guess(None)
        assert ok is False
        assert err == "Enter a guess."

    def test_valid_integer_is_parsed(self):
        ok, value, err = parse_guess("42")
        assert ok is True
        assert value == 42
        assert err is None

    def test_decimal_is_truncated_to_int(self):
        ok, value, err = parse_guess("7.9")
        assert ok is True
        assert value == 7

    def test_non_numeric_is_rejected(self):
        ok, value, err = parse_guess("abc")
        assert ok is False
        assert value is None
        assert err == "That is not a number."
