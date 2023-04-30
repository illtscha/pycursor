# pycursor
A python commandline library to install cursor packages on windows


# Getting Started
Download all files and go into the folder with the Setup.py file. From there, open up command prompt as administrator and type: 
```
pip install .
```
to install the package.

To run the program, type `pycursor <parameters>` into command prompt

# Parameters
## At least one is requiered
### `--byPath`
Opens one filedialog for every cursor in cursor pack. Just click cancel to not set a cursor and it will skip the certain cursor.

Requires `-p` or `--path` for the folder with the .cur or .ani files and `-n` or `--name` for the name of the cursor package.
### `--byName`
Uses Levenshtein Distance to match the cursor files with the system cursor files.

Requires `-p` or `--path` for the folder with the .cur or .ani files and `-n` or `--name` for the name of the cursor package.
### `--byFile`
Use the parameters:
--alternate
--handwriting 
--precision 
--link
--move 
--diagonal1
--diagonal2
--horizontal
--vertical=
--unavailable
--text
--busy
--working
--help
--normal
--person
--location

Requires `-p` or `--path` for the folder with the .cur or .ani files and `-n` or `--name` for the name of the cursor package.
### `--createCRS`

