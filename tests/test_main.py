"""Test cases for the __main__ module."""
import itertools
from pathlib import Path

import pytest
from click.testing import CliRunner

import tabelir
from tabelir import __main__


@pytest.fixture
def runner() -> CliRunner:
    """Fixture for invoking command-line interfaces."""
    return CliRunner()


@pytest.mark.parametrize("fluid", ["Nitrogen", "Methane", "CarbonDioxide"])
def test_main_with_no_output_dir_writes_tables_to_current_dir(
    runner: CliRunner, tmp_path: Path, fluid: str
) -> None:
    """Running in a temporary dir should create a folder."""
    with runner.isolated_filesystem(temp_dir=tmp_path):
        result = runner.invoke(__main__.main, fluid)

        assert result.exit_code == 0
        path = Path(fluid)
        assert path.exists()
        assert path.is_dir()


@pytest.mark.parametrize("fluid", ["Nitrogen", "Methane", "CarbonDioxide"])
def test_main_writes_all_files(runner: CliRunner, tmp_path: Path, fluid: str) -> None:
    """Running in a temporary dir should create a folder."""
    with runner.isolated_filesystem(temp_dir=tmp_path):
        runner.invoke(__main__.main, fluid)

        phases = list(tabelir.Phase)
        second_inputs = list(tabelir.SecondInput)
        properties = list(tabelir.ThermophysicalProperty)

        for phase, si, prop in itertools.product(phases, second_inputs, properties):
            filename = tabelir.filename_from(si, phase, prop)
            assert (Path(fluid) / filename).exists()
