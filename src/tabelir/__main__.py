"""Command-line interface."""
import click


@click.command()
@click.version_option(message="%(version)s")
def main() -> None:
    """Tabelir - Create fluid tables."""


if __name__ == "__main__":
    main()  # pragma: no cover
