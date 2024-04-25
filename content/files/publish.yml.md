+++
title = 'Publish.yml'
date = 2024-04-25T11:50:32-07:00
draft = false
weight = 4
+++

[Back to instructions](/Python_Tips/files/publishing/#add-action-script)

```yaml
# Name of the GitHub Actions workflow
name: Publish Python Package

# Define the GitHub event that triggers the workflow
on:
  push:
    branches:
      - master # The workflow triggers on pushes to the master branch; adjust if your default branch has a different name, like 'main'

# Define jobs that will be executed by the workflow
jobs:
  build-and-publish:
    # Specifies the type of virtual host machine to run the job on
    runs-on: ubuntu-latest # This job runs on the latest Ubuntu runner provided by GitHub

    # Steps represent a sequence of tasks that will be executed as part of the job
    steps:
      - uses: actions/checkout@v2 # Checks out your repository under $GITHUB_WORKSPACE, so your workflow can access it

      - name: Set up Python
        uses: actions/setup-python@v2 # This action sets up a Python environment
        with:
          python-version: "3.x" # Specify the Python version you need; 3.x will use the latest version of Python 3

      - name: Install dependencies
        run: | # Run commands using the default shell
          python -m pip install --upgrade pip # Upgrade pip to the latest version
          pip install setuptools wheel twine # Install packages needed to build and upload the Python package

      - name: Build and publish
        env:
          TWINE_USERNAME: __token__ # Username for PyPI, using a token instead of a username
          TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN }} # PyPI password, stored securely as a GitHub secret
        run: | # Execute a multi-line script
          python setup.py sdist bdist_wheel # Run setup.py to create a source distribution and wheel
          twine upload dist/* # Use twine to upload the distribution packages in the dist/ directory to PyPI
```
