"""Command-line interface."""

import click

from tabelir import TabelirApp


@click.command()
@click.version_option(message="%(version)s")
@click.argument("fluid")
def main(fluid: str) -> None:
    """Tabelir - Create fluid tables for given FLUID in the current dir.

    This dir and all its contents will be overwritten!
    """
    app = TabelirApp(fluid)
    app.run()


if __name__ == "__main__":
    main()  # pragma: no cover
