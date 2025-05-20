# cli/main.py
import click

from . import __version__
from .youtube import authenticate, build_service, get_recommendations


@click.group()
def app():
    """YouTube Codex CLI entry point."""
    pass


@app.command()
def version() -> None:
    """Show the package version."""
    click.echo(__version__)


@app.command()
def login() -> None:
    """Authenticate with YouTube via OAuth."""
    authenticate()
    click.echo("Authentication successful.")


@app.command()
def recommendations() -> None:
    """Display recommended videos for the logged-in user."""
    service = build_service()
    videos = get_recommendations(service)
    for video in videos:
        click.echo(f"{video['title']} - {video['url']}")


if __name__ == "__main__":
    app()
