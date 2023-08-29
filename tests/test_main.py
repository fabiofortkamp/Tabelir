"""Test cases for the __main__ module."""

from pathlib import Path

import pytest
from click.testing import CliRunner

from tabelir import __main__


@pytest.fixture
def runner() -> CliRunner:
    """Fixture for invoking command-line interfaces."""
    return CliRunner()


def test_main_with_no_argument_succeeds(runner: CliRunner) -> None:
    """It exits with a status code of zero. Default is methane."""
    result = runner.invoke(__main__.main)
    assert result.exit_code == 0


def test_main_with_no_argument_writes_tables_to_current_dir(
    runner: CliRunner, tmp_path
) -> None:
    """Running in a temporary dir should create a Methane folder."""
    with runner.isolated_filesystem(temp_dir=tmp_path):
        runner.invoke(__main__.main)

        assert Path("Methane").exists()
        assert Path("Methane").is_dir()
