# cli/main.py
import click


@click.group()
def app():
    """YouTube Codex CLI entry point."""
    pass


if __name__ == "__main__":
    app()
