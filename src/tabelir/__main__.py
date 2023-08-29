"""Command-line interface."""
from pathlib import Path

import click

from tabelir import TabelirApp


@click.command()
@click.version_option(message="%(version)s")
@click.argument("fluid")
@click.option(
    "-o",
    "--output-dir",
    "output_dir",
    default=Path.cwd(),
    show_default=True,
    type=click.Path(exists=True, file_okay=False, writable=True, path_type=Path),
    help="Directory where the new fluid library will be created",
)
def main(fluid: str, output_dir: Path) -> None:
    """Tabelir - Create fluid tables for given FLUID."""
    app = TabelirApp()
    app.run()


if __name__ == "__main__":
    main()  # pragma: no cover
