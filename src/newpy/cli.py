def run(argv: list[str]) -> None:
    if len(argv) < 2:
        print("Usage: newpy <project-name>")
        return

    project_name = argv[1]

    print(f"Creating project: {project_name}")
