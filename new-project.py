import os
import sys
import urllib.request

"""
Put this file in the folder that you want to create a new project in and run it with 'python new-project.py <project-name>'
"""


def create_file(text, filename):
    try:
        with open(filename, "w") as file:
            text = file.write(text)
            print(f"Created file {filename}")
    except:
        print(f"ERROR: Could not create file: {filename}")
        sys.exit(1)


def create_folder(folder_path):
    try:
        os.mkdir(folder_path)
        print(f"Created folder {folder_path}")
    except:
        print(f"ERROR: Could not create folder: {folder_path}")
        sys.exit(1)


def get_project_name():
    project_name = ""
    try:
        project_name = sys.argv[1]
    except:
        print("ERROR: Please provide a project name")
    return project_name


def create_app_file(folder):
    filename = os.path.join(folder, "app.py")
    text = f"""from {project_name} import app

if __name__ == "__main__":
    print(f"app: {{app}}")
"""
    create_file(text, filename)


def create_project_init_file(folder, project_name):
    filename = os.path.join(folder, "__init__.py")
    text = f"from .app import app"
    create_file(text, filename)


def create_project_app_file(folder):
    filename = os.path.join(folder, "app.py")
    text = 'app = "The App"'
    create_file(text, filename)


def create_tests_init_file(folder):
    filename = os.path.join(folder, "__init__.py")
    text = ""
    create_file(text, filename)


def create_tests_app_file(folder, project_name):
    filename = os.path.join(folder, "test_app.py")
    text = f"""
from minsonet import app


def test_app():

    assert app == "The App"

"""
    create_file(text, filename)


def create_conftest_file(folder):
    filename = os.path.join(folder, "conftest.py")
    text = ""
    create_file(text, filename)


def create_coveragerc_file(folder):
    filename = os.path.join(folder, ".coveragerc")
    text = """
[run]
branch=True

[report]
# Regexes for lines to exclude from consideration
exclude_lines =
    # Have to re-enable the standard pragma
    pragma: no cover

    # Don't complain about missing debug-only code:
    def __repr__
    if self\.debug

    # Don't complain if tests don't hit defensive assertion code:
    raise AssertionError
    raise NotImplementedError

    # Don't complain if non-runnable code isn't run:
    if 0:
    if __name__ == .__main__.:

ignore_errors = True

omit = .venv/*,tests/*,coverage/*,data/*,docs/*,rest-client/*

[html]
directory = coverage
"""
    create_file(text, filename)


def create_flake8_file(folder):
    filename = os.path.join(folder, ".flake8")
    text = """
[flake8]
max-line-length = 88
per-file-ignores = __init__.py:F401
ignore = E501 # exceeded max line length
"""
    create_file(text, filename)


def create_pip_file(folder):
    filename = os.path.join(folder, "Pipfile")
    text = """
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]

[dev-packages]
black = "*"
flake8 = "*"
isort = "*"
pytest = "*"
pytest-cov = "*"
python-dotenv = "*"
rope = "*"

[requires]
python_version = "3.8"

[pipenv]
allow_prereleases = true
"""
    create_file(text, filename)


def create_license_file(folder):
    filename = os.path.join(folder, "LICENSE")
    url = "https://gist.githubusercontent.com/bjanderson/163bf4e68e4c0cddada02d6fa7a6ceb6/raw/36ea31246ce4c4b3676a67a4dc5047a432db15a9/LICENSE"
    urllib.request.urlretrieve(url, filename)
    print(f"Downloaded LICENSE to {filename}")


def create_gitignore_file(folder):
    filename = os.path.join(folder, ".gitignore")
    url = "https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore"
    urllib.request.urlretrieve(url, filename)
    print(f"Downloaded .gitignore to {filename}")


project_name = get_project_name()
print(f"Creating: {project_name}")

print("Creating folders")
cwd = os.path.abspath(os.getcwd())
project_dir = os.path.join(cwd, project_name)
create_folder(project_dir)
app_dir = os.path.join(project_dir, project_name)
create_folder(app_dir)
tests_dir = os.path.join(project_dir, "tests")
create_folder(tests_dir)

print("Creating files")
create_app_file(project_dir)
create_project_init_file(app_dir, project_name)
create_project_app_file(app_dir)
create_tests_init_file(tests_dir)
create_tests_app_file(tests_dir, project_name)
create_flake8_file(project_dir)
create_conftest_file(project_dir)
create_coveragerc_file(project_dir)
create_pip_file(project_dir)
create_license_file(project_dir)
create_gitignore_file(project_dir)

print("The End")

print(
    "\nnow cd into your project and run 'pipenv install' and 'pipenv install --dev'\n"
)
