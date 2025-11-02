import click

from example_cli import calc

__all__ = ["calc"]


@click.command()
@click.option("--verbose", "-v", is_flag=True, help="Enable verbose output")
def main(verbose: bool) -> None:
    if verbose:
        click.echo("Running in verbose mode")
    print("Hello from example-cli!")


if __name__ == "__main__":
    main()
