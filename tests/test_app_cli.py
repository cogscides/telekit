from __future__ import annotations

import json
from pathlib import Path

from typer.testing import CliRunner

from app import app


runner = CliRunner()


def test_add_client_creates_local_client_registry(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    result = runner.invoke(app, ["add-client", "demo-session"])

    assert result.exit_code == 0
    clients_path = tmp_path / "data" / "clients.json"
    assert clients_path.exists()
    assert json.loads(clients_path.read_text(encoding="utf-8")) == [
        {
            "session_name": "demo-session",
            "commands": ["IngTranscribeCommand", "IngGPTCommand"],
        }
    ]


def test_help_explains_cli_surface():
    result = runner.invoke(app, ["--help"])

    assert result.exit_code == 0
    assert "Telekit is a Telegram self-automation client" in result.stdout
    assert "start-program" in result.stdout


def test_start_program_help_mentions_transcription_model():
    result = runner.invoke(app, ["start-program", "--help"])

    assert result.exit_code == 0
    assert "--transcription-model" in result.stdout
    assert "gpt-4o-mini-" in result.stdout
    assert "transcribe" in result.stdout
