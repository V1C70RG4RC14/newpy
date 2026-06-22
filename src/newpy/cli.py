import sys


def run() -> None:
    if len(sys.argv) < 2:
        print("Usage: newpy <project-name>")
        return

    project_name = sys.argv[1]

    print(f"Creating project: {project_name}")
