"""Test cases for the __main__ module."""
import itertools
from pathlib import Path

import numpy as np
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
    """Running in a temporary dir should create all files with the right specs."""
    with runner.isolated_filesystem(temp_dir=tmp_path):
        runner.invoke(__main__.main, fluid)

        phases = list(tabelir.Phase)
        second_inputs = list(tabelir.SecondInput)
        properties = list(tabelir.ThermophysicalProperty)

        for phase, si, prop in itertools.product(phases, second_inputs, properties):
            filename = tabelir.filename_from(si, phase, prop)
            with open(Path(fluid) / filename) as f:
                lines = f.readlines()

            header_values = lines[0].split(",")
            title = header_values[0].split("/")
            assert title == ["pressure", str(si)]

            assert len(header_values[1:]) == tabelir.N_SECOND_INPUT_POINTS
            assert len(lines[1:]) == tabelir.N_PRESSURE_POINTS

            second_input_line = " ".join(header_values[1:])
            second_input_values = np.fromstring(second_input_line, sep=" ")
            assert all(np.isfinite(second_input_values))

            pressure_values = np.array(float(line.split(",")[0]) for line in lines[1:])
            assert all(np.isfinite(pressure_values))

            prop_values = np.loadtxt(
                Path(fluid) / filename,
                dtype=float,
                delimiter=",",
                skiprows=1,
                usecols=tuple(range(1, tabelir.N_SECOND_INPUT_POINTS + 1)),
            )

            assert np.all(np.isfinite(prop_values))
