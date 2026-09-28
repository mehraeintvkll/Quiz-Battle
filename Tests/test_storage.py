from storage import ScoreBoard
import pytest



def test_is_empty(tmp_path) -> None:
    board = ScoreBoard((str(tmp_path / "leaderboard,json")))
    assert board.is_empty()

