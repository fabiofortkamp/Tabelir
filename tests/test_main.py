"""Test cases for the __main__ module."""

from pathlib import Path

import pytest
from click.testing import CliRunner

from tabelir import __main__


@pytest.fixture
def runner() -> CliRunner:
    """Fixture for invoking command-line interfaces."""
    return CliRunner()


def test_main_with_no_argument_writes_tables_to_current_dir(
    runner: CliRunner, tmp_path: Path
) -> None:
    """Running in a temporary dir should create a Methane folder."""
    with runner.isolated_filesystem(temp_dir=tmp_path):
        result = runner.invoke(__main__.main)

        assert result.exit_code == 0
        assert Path("Methane").exists()
        assert Path("Methane").is_dir()
