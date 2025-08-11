import pathlib
import sys

# Ensure the repository root is on the import path
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from multi_agent_demo import execute


def test_execute_runs_all_workers():
    result = execute("demo task")
    assert "Worker A" in result
    assert "Worker B" in result
    assert "demo task" in result
