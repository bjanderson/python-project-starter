# Python Project Starter

This script will set up a new python project for you.

It creates some basic config files, such as a gitignore, license, Pipfile, and some linting and testing configurations.

It also creates a simple project that you can run, just to verify that everything is working.

Simply put the `new-project.py` file in the folder that you want to create the project in and run it with

    python3 new-project.py <project-name>

Then `cd` into the &lt;project-name&gt; folder and run

    pipenv install
    pipenv install --dev

You should then be able to run the default project with

    python app.py

And be able to run the default test with

    pytest
