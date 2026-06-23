from newpy.cli import run


def test_run_without_arguments(capsys):
    run(["newpy"])

    captured = capsys.readouterr()

    assert captured.out == "Usage: newpy <project-name>\n"


def test_run_with_project_name(capsys):
    run(["newpy", "calculadora"])

    captured = capsys.readouterr()

    assert captured.out == "Creating project: calculadora\n"
