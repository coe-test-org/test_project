# test_project
testing out making a python package

# How to install the package

Open PowerShell terminal (or Ubuntu bash terminal)

1. Make a new folder
2. `pip install uv`
3. `uv venv --python 3.11`
4.  `.\.venv\Scripts\activate`
5. `uv pip install polars`
6. `uv pip install git+https://github.com/coe-test-org/test_project.git#egg=test_project`


# How to test it
create a script called `main.py` in your folder and run this code:

```python

from test_project import helpers
import polars as pl


df = pl.DataFrame({
    'date': [
        '2022-01-03',
        '01-02-2020',
        '44115',
        None,
        "2022-12-27 08:26:49",
        # "2022-12-27T08:26:49",
        '01/02/1995',
        '2/3/2022',
        '2/16/2022'
    ]
})

df_output = (
    df
    .with_columns(
        output_date = helpers.date_format('date')
    )
    .select('output_date')
)

print(df_output)
```

it should give you this output

```python
>>> print(df_output)
shape: (8, 1)
┌─────────────┐
│ output_date │
│ ---         │
│ date        │
╞═════════════╡
│ 2022-01-03  │
│ 2020-01-02  │
│ null        │
│ null        │
│ 2022-12-27  │
│ 1995-01-02  │
│ 2022-02-03  │
│ 2022-02-16  │
└─────────────┘
```


# For Devs - how to create a package with uv
1. In a new repo, run `uv init --package <package_name>`
	It gives you this:
```bash
.
├── LICENSE
├── README.md
└── test_package
    ├── README.md
    ├── pyproject.toml
    └── src
        └── test_package
            └── __init__.py

3 directories, 5 files

```
2. Create a venv with `uv venv`
  a. This creates a venv you can activate (called your package name)
	b. Creates a  `uv.lock` file 
	c. `Uv sync` to install and update your venv
3. Run `uv build` and it will build your package, adding a `dist/` folder with a `.tar.gz` file of the package.
	a. Amazing
	b. [follow these docs](https://docs.astral.sh/uv/guides/package/#publishing-your-package) to publish it to pypi or somewhere else privately 
4. To install from github: `uv pip install git+https://github.com/coe-test-org/test_project.git#egg=test_project`
If you get python version error, add python version to your .venv with `uv python install 3.11` or rebuild the venv with `uv venv --python 3.11`



