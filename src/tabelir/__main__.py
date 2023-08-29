"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Tabelir."""


if __name__ == "__main__":
    main(prog_name="Tabelir")  # pragma: no cover
