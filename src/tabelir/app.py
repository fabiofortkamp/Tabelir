"""app.py - Main app."""
import itertools
from pathlib import Path

import tabelir


class TabelirApp:
    """Main app to generate tables."""

    def __init__(self, fluid: str) -> None:
        """Initialize the main app.

        Args:
            fluid (str): fluid name; a directory with this name will be created.
        """
        self.fluid = fluid

    def run(self) -> None:
        """Generate tables from input arguments."""
        path = self.create_directory()
        self.create_filenames(path)

    def create_directory(
        self,
    ) -> Path:
        """Create directory for tables.

        Returns:
            Path: path to created directory.
        """
        path = Path(self.fluid)
        path.mkdir(exist_ok=True)
        return path

    def create_filenames(self, path: Path) -> None:
        """Create all relevant files, ready to be populated.

        Args:
            path (Path): directory where to create files.
        """
        phases = list(tabelir.Phase)
        second_inputs = list(tabelir.SecondInput)
        properties = list(tabelir.ThermophysicalProperty)

        for phase, si, prop in itertools.product(phases, second_inputs, properties):
            filename = tabelir.filename_from(si, phase, prop)
            Path(path / filename).touch()
