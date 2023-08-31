"""app.py - Main app."""
from pathlib import Path


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
        self.create_directory()

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
