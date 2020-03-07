import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


if __name__ == "__main__":

    if "{{ cookiecutter.generate_html }}" != "y":
        remove("todo/templates/application.html")

    if "{{ cookiecutter.start_from }}" != "Scaffolding":
        remove("tests/__init__.py")
        remove("tests/conftest.py")
        remove("tests/test_app.py")
        remove("docs")
