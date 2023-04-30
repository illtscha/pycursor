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

## `--byPath`
Opens a filedialog for every cursor in cursor pack. Just click cancel to not set a cursor and it will skip the certain cursor.

Example `pycursor --byPath --name Test --path "C:\Users\<Name>\Desktop\Text.cur"`

This will open a filedialog for every cursor in cursor pack. After you have selected every cursor, it will create a cursor theme that you can select in the Windows mouse settings by pressing `Win` + `R` and typing `main.cpl` or running the command `pycursor -o`. 
To select the Theme, go to the header `Pointers` and select your Theme in the `Schemes` dropdown.

Requires `-p` or `--path` for the folder with the `.cur` or `.ani` files and `-n` or `--name` for the name of the cursor package.
## `--byName`
Uses Levenshtein Distance to match the cursor files with the system cursors.

Requires `-p` or `--path` for the folder with the `.cur` or `.ani` files and `-n` or `--name` for the name of the cursor package.
## `--byFile`
Use the parameters:
```
--alternate
--handwriting 
--precision 
--link
--move 
--diagonal1
--diagonal2
--horizontal
--vertical
--unavailable
--text
--busy
--working
--help
--normal
--person
--location
```
with the corrisponding path to set cursors.

Example: `pycursor --byFile --alternate "C:\Users\<Name>\Desktop\Normal.cur" --text "C:\Users\<Name>\Desktop\Text.cur" --name Test --path "C:\Users\<Name>\Desktop"`

This will only set the Alternate and Text cursor. The cursor pack will be named Test and the cursor files are saved on Desktop.

If you want to skip a cursor file just dont specify it.


Requires `-p` or `--path` for the folder with the `.cur` or `.ani` files and `-n` or `--name` for the name of the cursor package.
## `--byCRS`
If you have a `.crs` file, you can install the cursor package with this command.

Requires `-p` or `--path` for the folder with the `.crs` file and `-n` or `--name` for the name of the cursor package.
## `--createCRS`
Requires one of the following:
#### `--byPath`
Opens one filedialog for every cursor in cursor pack. Just click cancel to not set a cursor and it will skip the certain cursor.

Requires `-p` or `--path` for the save folder and `-n` or `--name` for the name of the crs file.
#### `--byName`
Uses Levenshtein Distance to match the cursor files with the system cursors.

Requires `-p` or `--path` for the save folder and `-n` or `--name` for the name of the crs file.
#### `--byFile`
Use the parameters:
```
--alternate
--handwriting 
--precision 
--link
--move 
--diagonal1
--diagonal2
--horizontal
--vertical
--unavailable
--text
--busy
--working
--help
--normal
--person
--location
```
with the corrisponding path to set cursors.

Example: `pycursor --createCRS --byFile --alternate "C:\Users\<Name>\Desktop\Normal.cur" --text "C:\Users\<Name>\Desktop\Text.cur" --name Test --path "C:\Users\<Name>\Desktop"`

This will merge the Alternate and Text cursor into an `.crs` file. The cursor pack will be named Test and the cursor files are saved on Desktop.

If you want to skip a cursor file just dont specify it.

Requires `-p` or `--path` for the save folder and `-n` or `--name` for the name of the crs file.


## `-o` or `--open`
Opens the Windows mouse settings at the end so you can set the Cursor Theme.
