# pip package demo

This repo shows a minimal example how to create python package with tests,
documentation and packaging settings.

- [Files and folders](#files-and-folders)
- [Installation](#installation)
  - [Install the package](#install-the-package)
  - [Dependencies](#dependencies)
  - [development](#development)
- [Distribute the package](#distribute-the-package)
  - [Create the package distribution files](#create-the-package-distribution-files)
  - [upload the package distribution files](#upload-the-package-distribution-files)
  - [Create new versions](#create-new-versions)
- [Run the test](#run-the-test)
  - [coverage](#coverage)
- [Documentation](#documentation)

## Files and folders

The following files and folders are contained within this folder (or will be created during setup or tests):

```text
pip_package_demo
│
│   LICENSE
│   README.md
│   dev_reqs.txt
│   setup.cfg
│   setup.py
│ 
├───dist
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
├───pmdemo
│       __init__.py
│       __main__.py
│       my_mod.py
│
└───tests
        test_my_module.py
```

| folder name     | description                                 | contained in the distributed package |
| --------------- | ------------------------------------------- | ------------------------------------ |
| `LICENSE`       | license according to your needs or rights   | yes                                  |
| `README.md`     | for the repository welcome screen           | yes (in PKG-INFO)                    |
| `dev_reqs.txt`  | list of dependencies for development        | no                                   |
| `setup.cfg`     | information about the package + settings *3 | yes                                  |
| `setup.py`      | needed for editable install                 | yes                                  |
| `.git`          | for git source control                      | no                                   |
| `dist/` *2      | package distribution files                  | no                                   |
| `doc/` files    | created by sphinx to build docs             | no *1                                |
| `doc/output` *2 | sphinx output products (e.g. html, pdf)     | no *1                                |
| `doc/source`    | additional sphinx source code in rst        | no *1                                |
| `htmlcov` *2    | coverage report in html                     | no                                   |
| `src`           | python source code of the package           | yes                                  |
| `tests`         | container of the package tests              | no *1                                |

*1: depends on the `package_data` and `data_files` settings of `setup.cfg`,
it may be a good idea to include these too

*2: not included in the repo,
but will be created once documentation, pytest coverage is created.

*3: linter or other settings

## Installation

I suggest to use the conda package manager to maintain environments. Once you
installed [miniconda](https://docs.conda.io/en/latest/miniconda.html), even as
a user, start an activated prompt (like the Anaconda Prompt), create and
activate a new environment.

### Install the package

You can install

1. **from the source code, locally, for development**. In the root,
   issue `pip install -e .` This will place a link
   to your python `site-packages` folder which will tell to look
   for the library's content not directly in the `site-packages`,
   but where you cloned the repo. You need to manually add the git_subm_demo
   package.
2. **from a package distribution you already have locally**.
   This can happen if you download the package distribution files, somebody sent you the files or you create the package files yourself (see below).
   Useful if pip and python doesn't have internet access
   due to firewall settings. If the package files are in
   `pip_package_demo\dist\"`, you can install it with

   ```text
   (pip_demo) PS C:\Users\daniel\source\repos\pip_package_demo> pip install .\dist\pip_package_demo-1.0.9-py3-none-any.whl 
   Processing  c:\users\daniel\source\repos\pip_package_demo\dist\pip_package_demo-1.0.9-py3-none-any.whl
   Collecting numpy>=1.19.1
   Using cached numpy-1.20.3-cp39-cp39-win_amd64.whl (13.7 MB)
   Installing collected packages: numpy, pip-package-demo
   Successfully installed numpy-1.20.3 pip-package-demo-1.0.9
   (pip_demo) PS C:\Users\daniel\source\repos\pip_package_demo>
   ```

3. **using pip and a remote repository**.
   The aim of this package is to be able to install this package with pip.
   This package is (was) available on [test.pypi.org](https://test.pypi.org/project/pip-package-demo/),
   and it is (was) possible to install it with
   `pip install -i https://test.pypi.org/simple/pip-package-demo`

### Dependencies

The packages has 1 dependency, numpy,
which is installed together with this package automatically by pip if installed
locally or from a repository which has numpy.
Since [test.pypi.org](https://test.pypi.org/project/pip-package-demo/) is a
testing repo only, numpy is not available and you need to satisfy this
requirement by manually installing it.
Once the package is deployed to a repo where numpy is also available,
the package together with its dependencies will be possible to get installed.

### development

To develop this package, one needs linter, testing, documenting,
and packaging tools. The tools I used can be installed:
`pip install -r dev_reqs.txt`

## Distribute the package

The purpose of this repo is to show how to create the package
that can be installed in the way noted above.
This package uses namespace packages,
and settings regarded this are noted with comments in the source code.

### Create the package distribution files

To create the package distribution files, issue

```text
(pip_demo) PS C:\Users\daniel\source\repos\pip_package_demo> python -m build
```

This command produces a lot of output onto the terminal and creates the files

```text
├───dist
│       pip_package_demo-1.0.10-py3-none-any.whl
│       pip_package_demo-1.0.10.tar.gz
```

The version number reflects the value of `__version__` within the python file.
Take a look into the `.gz` file where you can see what is included in the
package. The `whl` file is binary.

### upload the package distribution files

You need the twine tool to upload your package and also need an account on the repository page (at least, on pypi.org or test.pypi.org). After that, you can upload your package with

```text
(pip_demo) PS C:\Users\daniel\source\repos\pip_package_demo> twine upload --repository testpypi dist/*
Uploading distributions to https://test.pypi.org/legacy/
Enter your username: tuzesdaniel
Enter your password: 
Uploading pip_package_demo-1.0.10-py3-none-any.whl
100%|██████████████████████████████████████████████████████████████| 19.0k/19.0k [00:01<00:00, 9.73kB/s] 
Uploading pip_package_demo-1.0.10.tar.gz
100%|██████████████████████████████████████████████████████████████| 19.3k/19.3k [00:01<00:00, 14.9kB/s] 

View at:
https://test.pypi.org/project/pip-package-demo/1.0.10/
(pip_demo) PS C:\Users\daniel\source\repos\pip_package_demo>
```

Now the package is (was) available at [test.pypi.org](https://test.pypi.org/project/pip-package-demo).

### Create new versions

You cannot make any modification to an already uploaded version, you need to create a new one.

1. Modify the version number (defined in `setup.cfg`, and in this case, the setup reads this value from `pmdemo/my_mod.py`), follow the rules of the [naming conventions](https://semver.org/#summary)
2. Create a new package with the same command `python -m build`
3. and upload only the new files, e.g. by deleting all but the newest 2 files from the `dist` folder

If you really want to overwrite a version, you need to delete the project from the repository and recreate it again.

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

test\test_my_module.py .                                            [100%] 

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

test\test_my_module.py .                                                                            [100%] 

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
   found in [`dev_reqs.txt`](requirements.txt)
2. issue `make html` in the `doc` folder to generate the html documentation.

To create documentation for a project, one needs to prepare the followings:

- create docstrings in the python files of the package.
  In this case, the only module in the package is
  [`my_mod.py`](pmdemo/my_mod.py),
  so the docstring are in this file.
- [create settings](https://www.sphinx-doc.org/en/master/usage/quickstart.html#setting-up-the-documentation-sources) in the `doc` folder. The settings
  in this example are stored in the [`conf.py`](doc/source/conf.py),
  but it can be included in [`setup.cfg`](setup.cfg) too, see
  [sphinx's webpage](https://www.sphinx-doc.org/en/master/usage/advanced/setuptools.html?highlight=project%20release#using-setuptools-integration).
- Add further documentations, e.g. how to install the package,
  who created it, where to get help, etc.

The documentation is distributed independently of the source code, and can hosted
on a fancy site.
