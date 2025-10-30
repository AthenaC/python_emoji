# tests/test_smoke.py
import subprocess
import sys


def test_script_runs_and_prints_emoji():
    """Test that the script runs and prints an emoji."""
    result = subprocess.run(
        [
            sys.executable, 
            "../make_emoji.py", 
            "--name", ":sparkles:", 
            "--msg", "Hello"
        ],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "✨" in result.stdout  # sparkles emoji