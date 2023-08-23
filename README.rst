BCBB Package Template for Python
++++++++++++++++++++++++++++++++

The "BCBB Package Template" project provides a skeleton structure for new Python packages and projects which contains
an advanced starting point for continuous integration, configuration, software quality and implementations for best
practices for modern Python project development. The project is configured with Github Actions support the following:

* Linting is done with `pre-commit <https://pre-commit.com>`_ which is configured to use several Python tools.
    * The automatic uncompromising code formatter `Black <https://black.readthedocs.io/en/stable/>`_.
    * The style enforcement tool `flake8 <https://flake8.pycqa.org/en/latest/>`_.
    * and some pre-commit check for credentials, and excessively large file.
    * Automatically run on pull requests and locally on commits.
* Testing is performed with `pytest <https://docs.pytest.org]>`_.
    * Automatically run on pull requests and updates to the `main` branch.
* Documentation uses `Sphinx <https://www.sphinx-doc.org/>`_.
    * Uses the `reSTructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_ format.
    * Sphinx is configured to automatically document the classes and procedures (API) defined.
    * Automatically published on the `main` branch updates.
* Build Python packages as `wheels <https://www.google.com/search?client=safari&rls=en&q=python+wheels&ie=UTF-8&oe=UTF-8>`_.
    * Built as artifacts on `main` branch updates.
* Publish Releases
    * Releases are automatically triggered with a push for git tags matching `v*`.
    * Artifacts automatically published to GitHub Releases, and to NIAID's artifactory under bcbb-pypi.



.. image:: https://github.com/niaid/rap_py_template/actions/workflows/main.yml/badge.svg?branch=master
   :target: https://github.com/niaid/rap_py_template/actions/workflows/main.yml
   :alt: Master Build Status


Sphinx docs: https://cautious-umbrella-90d21757.pages.github.io/