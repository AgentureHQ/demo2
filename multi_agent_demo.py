"""A simple multi-agent collaboration demo.

This module defines several basic agents that work together to perform a
user-provided task. It is designed for demonstration and educational
purposes only.
"""

from dataclasses import dataclass
from typing import List


@dataclass
class Agent:
    """Base class for all agents."""
    name: str

    def run(self, *args, **kwargs):
        """Perform the agent's action."""
        raise NotImplementedError


class PlannerAgent(Agent):
    """Creates a simple plan for the given task."""
    def __init__(self) -> None:
        super().__init__("Planner")

    def run(self, task: str) -> List[str]:
        """Return a list of high-level steps for completing *task*."""
        return [
            f"Understand the task: {task}",
            f"Work on the task: {task}",
            "Compile the results",
        ]


class WorkerAgent(Agent):
    """Executes a single step from the planner."""
    def run(self, step: str) -> str:
        return f"{self.name} completed step: {step}"


class ReporterAgent(Agent):
    """Aggregates the results from workers."""
    def __init__(self) -> None:
        super().__init__("Reporter")

    def run(self, results: List[str]) -> str:
        summary = "Collaboration finished:\n" + "\n".join(results)
        return summary


def execute(task: str) -> str:
    """Run all agents to complete *task* and return a summary."""
    planner = PlannerAgent()
    steps = planner.run(task)

    workers = [WorkerAgent("Worker A"), WorkerAgent("Worker B")]
    results = []
    for i, step in enumerate(steps):
        worker = workers[i % len(workers)]
        results.append(worker.run(step))

    reporter = ReporterAgent()
    return reporter.run(results)


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        user_task = " ".join(sys.argv[1:])
    else:
        user_task = input("Enter a task: ")

    output = execute(user_task)
    print(output)
