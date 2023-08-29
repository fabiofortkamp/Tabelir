"""Command-line interface."""
import click

from tabelir import TabelirApp


@click.command()
@click.version_option(message="%(version)s")
def main() -> None:
    """Tabelir - Create fluid tables."""
    app = TabelirApp()
    app.run()


if __name__ == "__main__":
    main()  # pragma: no cover
