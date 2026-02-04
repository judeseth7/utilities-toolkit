# Utilities Toolkit ⚙️

This repository is a lightweight toolkit of small, focused command-line utilities. Each Python file in this repo is a self-contained "tool" you can run directly or import into other projects. Currently included tools:

- `password-generator.py` — simple random password generator 🔐
- `unit-converter.py` — interactive unit converter (length, temperature, weight) 🔁
- `organiser.py` — lightweight folder organizer (sorts files into type folders) 🗂️

---

## Password Generator 🔐

**Simple password generator** that creates a random password composed of letters, digits, and punctuation.

### Features ✅
- Generates a password of user-specified length
- Uses `string.ascii_letters`, `string.digits`, and `string.punctuation`
- Minimal, easy-to-read single-file script (`password-generator.py`)

### Requirements ⚙️
- Python 3.6+
- No external libraries required

### Usage ▶️
Run the script from the command line:

```bash
python password-generator.py
```

You will be prompted to enter the desired password length:

```
Enter password length: 12
# -> Example output: `fR3$k2!q9PL@`
```

### Use as a module 🔧
You can import the `generate_password` function into other Python code:

```python
from password_generator import generate_password
pw = generate_password(16)
print(pw)
```

> Note: If you import the file directly, make sure to adjust the import path (module name may differ depending on your package layout).

### Security note ⚠️
This script uses Python's `random.choice`, which is **not** suitable for cryptographic or high-security password generation. For security-sensitive uses, prefer the `secrets` module:

```python
import secrets
import string
pool = string.ascii_letters + string.digits + string.punctuation
secure_pw = ''.join(secrets.choice(pool) for _ in range(length))
```

---

## Unit Converter 🔁

**Interactive unit converter** that supports conversions for length, temperature, and weight.

### Features ✅
- Length: kilometers ↔ miles (`km`, `miles`)
- Temperature: Celsius ↔ Fahrenheit (`celsius`, `fahrenheit`)
- Weight: kilograms ↔ pounds (`kg`, `lbs`)
- Simple interactive menu-driven CLI (`unit-converter.py`)

### Usage ▶️
Run the script from the command line:

```bash
python unit-converter.py
```

Example interaction:

```
--- Welcome to Unit Converter ---
Menu:
1. Length
2. Temperature
3. Weight
Select dimension number: 1
Enter value to be converted: 5
Enter unit of value to be converted: km
# -> Example output: 3.106855
```

### Functions 📚
- `convert_length(value, choice)` — converts between kilometers and miles. Accepts `choice` as `"km"` or `"miles"` and returns the converted float or `None` for invalid units.
- `convert_temperature(value, choice)` — converts between Celsius and Fahrenheit. Accepts `choice` as `"celsius"` or `"fahrenheit"`.
- `convert_weight(value, choice)` — converts between kilograms and pounds. Accepts `choice` as `"kg"` or `"lbs"`.

### Use as a module 🔧
You can import and use conversion functions directly:

```python
from unit_converter import convert_length, convert_temperature
print(convert_length(10, "km"))        # kilometers -> miles
print(convert_temperature(32, "fahrenheit"))  # fahrenheit -> celsius
```

### Notes & Validation ⚠️
- The CLI expects the unit choice strings shown above (case-insensitive where `.lower()` is used in the script).
- Conversion functions return `None` for unsupported unit strings — handle this in callers.
- Results are returned as floats; format the output as desired for display.

---

## Organiser 🗂️

**Lightweight folder organizer** that sorts files into folders by extension.

### Features ✅
- Moves files into type-specific folders based on extension
- Configurable `FILE_TYPES` mapping to adjust categories
- Creates destination folders as needed and prints moved files

### Usage ▶️
Run the script from the folder you want to organize (or change the `FOLDER` constant in the script):

```bash
python organiser.py
```

Example output:

```
Moved example.png → Images
Moved report.pdf → PDFs
```

### Use as a module 🔧
You can import and call `organize_folder` from other Python code:

```python
from organiser import organize_folder
organize_folder()
```

---
## Improvements / Ideas 💡

- **`organiser.py`:**
	- Add a CLI with flags: `--folder` / `--target`, `--dry-run` (preview), `--recursive`, and `--ignore` patterns.
	- Support a configuration file (JSON/YAML) for `FILE_TYPES` mappings and ignore lists.
	- Provide conflict-handling policies: `rename` (auto-increment), `skip`, or `overwrite` (with optional confirmation).
	- Implement a safe staging/undo workflow (log moves, or move to a temporary staging folder then finalize) so operations can be reversed.
	- Offer MIME-based detection (via `mimetypes` or `python-magic`) and treat extensions case-insensitively.
	- Add `--dry-run` mode and verbose logging; optionally show a progress bar for large directories (`tqdm`).
	- Add unit tests that create sample files in a temp directory and verify folder organization and conflict handling.

- **`password-generator.py`:**
	- Offer a secure mode using the `secrets` module (`--secure`) and flags for toggling character classes (upper, lower, digits, symbols) and length.
	- Add an option to copy generated passwords to clipboard (`pyperclip`) and an option to output machine-readable formats for scripting.

- **`unit-converter.py`:**
	- Add non-interactive CLI arguments for direct conversions (e.g., `--from 10km --to miles`).
	- Expand supported units and improve parsing; consider integrating `pint` for robust unit handling.
	- Add conversion table unit tests and examples.

- **Performance & robustness:**
	- Handle large directories efficiently (batch moves, streaming, optional threading), validate inputs thoroughly, and add clear error messages.

## Requirements ⚙️
- Python 3.6+
- No external libraries required

