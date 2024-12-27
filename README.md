# CodeFuse

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Top Language](https://img.shields.io/github/languages/top/arvedb/CodeFuse?color=56BEB8)
![Repo Size](https://img.shields.io/github/repo-size/arvedb/CodeFuse?color=green)
![Last commit](https://img.shields.io/github/last-commit/arvedb/CodeFuse)
![Commit Activity](https://img.shields.io/github/commit-activity/m/arvedb/CodeFuse)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Command-Line Interface](#command-line-interface)
  - [Examples](#examples)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Overview

**CodeFuse** is a Python-based command-line tool designed to automatically combine all code files from a specified directory and its subdirectories into a single consolidated file. This utility simplifies the process of merging large codebases, enabling easier analysis, script reviews, and preparation of code for text-based processing or submission to large language models (LLMs).

## Features

- **Automatic File Aggregation:** Recursively scans specified directories to collect and merge code files based on customizable templates.
- **Template-Based Filtering:** Include or exclude files based on their extensions using predefined or custom templates.
- **Flexible Output Options:** Output the combined code to a file or directly to the clipboard for quick access.
- **Customizable Templates:** Easily define which file types to include or exclude, enhancing control over the merging process.
- **Error Handling:** Gracefully handles file read/write errors with informative messages.
- **Extensible:** Easily extendable to support additional features and integrations.

## Installation

### Prerequisites

- **Python 3.7 or higher** must be installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Clone the Repository

```bash
git clone https://github.com/arvedb/CodeFuse.git
cd CodeFuse
```

### Install Dependencies

It's recommended to use a virtual environment to manage dependencies.

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Unix or MacOS:
source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt
```

**Note:** If `requirements.txt` is not provided, install the necessary packages manually:

```bash
pip install argparse pyperclip
```

### Install CodeFuse

For development purposes, it's best to install CodeFuse in **editable mode**. This allows you to make changes to the source code without needing to reinstall the package each time.

```bash
pip install -e .
```

**Explanation:**

- `-e` or `--editable`: Installs the package in editable mode.
- `.`: Specifies the current directory as the source for the package.

After installation, the `codefuse` command will be available in your environment.

## Usage

Once installed, CodeFuse can be used via the `codefuse` command in your terminal or command prompt.

### Command-Line Interface

```bash
codefuse [OPTIONS] folder
```

### Arguments and Options

- **folder** (positional):  
  Path to the directory to be processed. Defaults to the current directory (`.`) if not specified.

- **-t**, **--template**:  
  Specify a template that determines which files to include or exclude. Defaults to the predefined `default_template`.

- **-i**, **--include**:  
  List of file extensions to include (e.g., `.py`, `.md`, `.txt`). This option is an alternative to using a template.

- **-e**, **--exclude**:  
  List of file extensions to exclude (e.g., `.py`, `.md`, `.txt`). This option is an alternative to using a template.

- **-o**, **--output**:  
  Path to the output file. If specified without a value, defaults to `output.txt`.

- **-c**, **--clipboard**:  
  Copy the combined output directly to the clipboard.

### Examples

1. **Combine All Python and Markdown Files in the Current Directory:**

   ```bash
   codefuse . -i .py .md
   ```

2. **Combine All Files Excluding `.txt` and `.json` Extensions:**

   ```bash
   codefuse /path/to/project -e .txt .json
   ```

3. **Specify a Custom Output File:**

   ```bash
   codefuse ./my_code -o combined_code.md
   ```

4. **Copy Combined Output to Clipboard:**

   ```bash
   codefuse ./scripts -c
   ```

5. **Using a Custom Template:**

   ```bash
   codefuse ./app -t custom_template
   ```

### Running Without Installation (Not Recommended)

If you prefer not to install the package (even in editable mode), you can run the CLI using Python's module execution. However, this method is less straightforward and generally not recommended for regular development workflows.

```bash
python -m codefuse . -i .py -c
```

**Note:** Ensure you are in the project root directory when running this command.

## Configuration

CodeFuse uses templates to determine which files to include or exclude during the merging process. By default, the `default_template` includes files with the following extensions:

```python
default_template = Template(
    include_extensions=[".py", ".md", ".txt", ".json", ".yaml", ".yml"]
)
```

### Creating Custom Templates

You can create custom templates by modifying the `templates.py` file or by passing template configurations through the CLI.

```python
from codefuse.templates import Template

custom_template = Template(
    include_extensions=[".js", ".html", ".css"]
)
```

**Note:** A template must specify either `include_extensions` or `exclude_extensions`, not both.

## Contributing

I welcome contributions from the community! Please read the [Contributing Guidelines](CONTRIBUTING.md) to get started.
## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any questions, suggestions, or support, please open an issue on the [GitHub repository](https://github.com/arvedb/CodeFuse) or contact [71208362+arvedb@users.noreply.github.com](mailto:71208362+arvedb@users.noreply.github.com).
