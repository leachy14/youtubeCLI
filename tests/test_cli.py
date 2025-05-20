from __future__ import annotations

from unittest.mock import patch

from click.testing import CliRunner

from cli.main import app


def test_help() -> None:
    runner = CliRunner()
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "YouTube Codex CLI" in result.output


def test_login_invokes_authenticate() -> None:
    runner = CliRunner()
    with patch("cli.main.authenticate") as auth:
        result = runner.invoke(app, ["login"])
        assert result.exit_code == 0
        auth.assert_called_once()


def test_recommendations() -> None:
    runner = CliRunner()
    videos = [
        {"title": "Video1", "url": "https://youtu.be/1"},
        {"title": "Video2", "url": "https://youtu.be/2"},
    ]
    with (
        patch("cli.main.build_service") as build_service,
        patch("cli.main.get_recommendations", return_value=videos) as get_recs,
    ):
        result = runner.invoke(app, ["recommendations"])
        assert result.exit_code == 0
        build_service.assert_called_once()
        get_recs.assert_called_once()
        assert "Video1" in result.output
        assert "Video2" in result.output
