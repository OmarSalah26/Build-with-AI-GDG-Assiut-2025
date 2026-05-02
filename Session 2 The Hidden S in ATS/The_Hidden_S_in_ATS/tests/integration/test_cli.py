import pytest
from gemini_ats_scorer.cli import main

def test_cli_requires_arguments(capsys):
    with pytest.raises(SystemExit):
        main([])
    captured = capsys.readouterr()
    assert "error: the following arguments are required" in captured.err
