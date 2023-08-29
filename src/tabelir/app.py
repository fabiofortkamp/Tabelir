"""app.py - Main app."""
from pathlib import Path


class TabelirApp:
    """Main app to generate tables."""

    def run(self) -> None:
        """Generate tables from input arguments."""
        self.create_directory()

    def create_directory(
        self,
    ) -> Path:
        """Create directory for tables.

        Returns:
            Path: path to created directory.
        """
        path = Path("Methane")
        path.mkdir()
        return path
