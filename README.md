# pip package demo

This repo shows a minimal example how to create python package with tests,
documentation and packaging settings.

- [pip package demo](#pip-package-demo)
  - [Files and folders](#files-and-folders)
  - [Installation](#installation)
    - [Install the package](#install-the-package)
    - [Dependencies](#dependencies)
  - [Create the package](#create-the-package)
  - [Run the test](#run-the-test)
    - [coverage](#coverage)
  - [Documentation](#documentation)

## Files and folders

The following files and folders are contained within this repo:

```text
│   pyproject.toml
│   README.md
│   requirements.txt
│   setup.cfg
│ 
├───doc
│   │   make.bat
│   │   Makefile
│   │
│   ├───build
│   │
│   └───source
│           conf.py
│           index.rst
│           installation.rst
│           module_doc.rst
│           release_notes.rst
│
├───htmlcov
│       index.html
│   
├───src
│   └───daniels_package
│           daniels_module.py
│
└───test
        test_daniels_module.py
```

| folder name        | description                                 | contained in the package |
| ------------------ | ------------------------------------------- | ------------------------ |
| `pyproject.toml`   | information about the packaging tool        | no                       |
| `README.md`        | for the repository welcome screen           | yes                      |
| `requirements.txt` | dependencies for development                | no                       |
| `setup.cfg`        | information about the package + settings *3 | no                       |
| `.git`             | for git source control                      | no                       |
| `doc/` files       | created by sphinx to build docs             | no                       |
| `doc/output`       | sphinx output products (e.g. html, pdf)*2   | no                       |
| `doc/source`       | additional sphinx source code in rst        | no                       |
| `htmlcov`          | coverage report in html *2                  | no                       |
| `src`              | python source code of the package           | yes                      |
| `test`             | is the container of the package tests.      | yes *1                   |

*1: depends on the settings of `setup.cfg`

*2: doesn't contained in the repo,
but will be created once documentation and pytest coverage is created.

*3: it can contain linter (pylint, pylama), testing (pytest, unittest)
and documentation (sphinx) settings.

## Installation

I suggest to use the conda package manager to maintain environments. Once you
installed [miniconda](https://docs.conda.io/en/latest/miniconda.html), even as
a user, start an activated prompt (like the Anaconda Prompt), create and
activate a new environment.

### Install the package

You can install

- from the source code, locally, for development. In the root,
  issue `pip install -e .` This will place a link
  to your python `site-packages` folder which will tell to look
  for the library's content not directly in the `site-packages`,
  but where you cloned the repo.
- from a package distribution you already have locally.
  This can happen if you download the package or somebody sent you as a file.
  Useful if pip and python doesn't have internet access
  due to firewall settings.
- using pip directly.
  The aim with this package is achieve this.
  You won't find this package on [pypi.org](http://pypi.org),
  but the package has been uploaded to test folders.

### Dependencies

The packages has 1 dependency, numpy,
which is installed together with this package automatically by pip.

To develop this package, one needs linter, testing, documenting,
and packaging tools. The tools I used can be installed

## Create the package

The purpose of this repo is to show how to create the package
that can be installed in the way noted above. TODO

## Run the test

Once you have installed the package and have all the requirements installed,
you can run the test with pytest directly from the root:

```text
(pip_demo) PS C:\Users\username\source\repos\pip_package_demo> pytest
============================= test session starts =============================
platform win32 -- Python 3.9.5, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: C:\Users\username\source\repos\pip_package_demo
plugins: pylama-7.7.1, cov-2.12.0
collected 1 item

test\test_daniels_module.py .                                            [100%] 

============================== 1 passed in 0.20s ============================== 
(pip_demo) PS C:\Users\username\source\repos\pip_package_demo>
```

### coverage

To create both html and xml coverage reports, issue

```text
(pip_demo) PS C:\Users\username\source\repos\pip_package_demo> pytest --cov --cov-report html --cov-report xml     
============================================= test session starts =============================================
platform win32 -- Python 3.9.5, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: C:\Users\username\source\repos\pip_package_demo
plugins: pylama-7.7.1, cov-2.12.0
collected 1 item

test\test_daniels_module.py .                                                                            [100%] 

----------- coverage: platform win32, python 3.9.5-final-0 -----------
Coverage HTML written to dir htmlcov
Coverage XML written to file coverage.xml


============================================== 1 passed in 0.42s ============================================== 
(pip_demo) PS C:\Users\username\source\repos\pip_package_demo>
```

The html report will be available in `htmlcov/index.html`, and the `coverage.xml` in the root can be used by other tools such as IDEs (like VS Code) to visualize the code coverage.

## Documentation

The necessary files for documentation is included in the repo.
To create pretty formatted documentation, one needs to generate by
calling the make from the doc folder. On Windows,

1. Use your new environment, where you have installed all the requirements
   found in [`requirements.txt`](requirements.txt)
2. issue `make html` in the `doc` folder to generate the html documentation.

To create documentation for a project, one needs to prepare the followings:

- create docstrings in the python files of the package.
  In this case, the only module in the package is
  [`daniels_module.py`](src/daniels_package/daniels_module.py),
  so the docstring are in this file.
- [create settings](https://www.sphinx-doc.org/en/master/usage/quickstart.html#setting-up-the-documentation-sources) in the `doc` folder. The settings
  in this example are stored in the [`conf.py`](doc/source/conf.py),
  but it can be included in [`setup.cfg`](setup.cfg) too, see
  [sphinx's webpage](https://www.sphinx-doc.org/en/master/usage/advanced/setuptools.html?highlight=project%20release#using-setuptools-integration).
- Add further documentations, e.g. how to install the package,
  who created it, where to get help, etc.

The documentation is distributed independently of the source code, and hosted
on a fancy site.
