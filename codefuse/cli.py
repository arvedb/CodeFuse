"""
CodeFuse Command-Line Interface (CLI) Module.

This module provides the command-line interface for the CodeFuse tool,
which is designed to merge multiple code files from a specified directory
into a single consolidated file. It handles parsing command-line arguments,
configuring templates for file inclusion/exclusion, and executing the merging process.
"""

import argparse
from .codefuse import CodeFuse
from .templates import Template, default_template


def setup_parser() -> argparse.ArgumentParser:
    """
    Configure and return the argument parser for the CodeFuse CLI.

    This function sets up the command-line arguments that CodeFuse accepts,
    including options for templates, file inclusion/exclusion, output paths,
    and clipboard operations.

    Returns:
        argparse.ArgumentParser: The configured argument parser.
    """
    parser = argparse.ArgumentParser(
        description="CodeFuse command line interface for merging code files into a single file."
    )

    parser.add_argument(
        "folder",
        nargs='?',
        default=".",
        type=str,
        help="Path to the directory to be processed. Defaults to the current directory ('.') if not specified.",
    )

    parser.add_argument(
        "-t",
        "--template",
        type=str,
        default=None,
        help="Template that determines which files to include or exclude. Defaults to 'default_template' if not provided.",
    )

    parser.add_argument(
        "-i",
        "--include",
        nargs="+",
        default=[],
        help="List of file extensions to include (e.g., .py .md .txt). This is an alternative to using a template.",
    )

    parser.add_argument(
        "-e",
        "--exclude",
        nargs="+",
        default=[],
        help="List of file extensions to exclude (e.g., .py .md .txt). This is an alternative to using a template.",
    )

    parser.add_argument(
        "-o",
        "--output",
        nargs="?",
        const="output.txt",
        default=None,
        type=str,
        help="Path to the output file. If specified without a value, defaults to 'output.txt'.",
    )

    parser.add_argument(
        "-c",
        "--clipboard",
        action="store_true",
        help="Copy the combined output directly to the clipboard.",
    )

    return parser


def main():
    """
    Entry point for the CodeFuse CLI.

    This function parses command-line arguments, configures the merging template
    based on the provided options, executes the merging process, and handles
    output operations such as writing to a file or copying to the clipboard.
    """
    # Set up and parse command-line arguments
    parser = setup_parser()
    args = parser.parse_args()

    # Determine the template to use based on provided arguments
    if args.template:
        # TODO: Implement loading of predefined templates based on the 'template' argument
        # For simplicity, using 'default_template' as a placeholder
        template = default_template
    elif args.include:
        template = Template(include_extensions=args.include)
    elif args.exclude:
        template = Template(exclude_extensions=args.exclude)
    else:
        # Use the default template if no specific options are provided
        template = default_template

    # Initialize the CodeFuse instance with the target folder and chosen template
    codefuse = CodeFuse(folder=args.folder, template=template)

    # Handle clipboard operation if the '-c' or '--clipboard' flag is set
    if args.clipboard:
        try:
            import pyperclip
            pyperclip.copy(codefuse.output)
            print("Combined code has been copied to the clipboard.")
        except Exception as e:
            print(f"Error copying to clipboard: {e}")

    # Handle output file writing if the '-o' or '--output' option is provided
    if args.output:
        try:
            codefuse.write_output(path=args.output)
            print(f"Combined code has been written to {args.output}")
        except Exception as e:
            print(f"Error writing to {args.output}: {e}")

    # If neither clipboard nor specific output is requested, print the combined output to the console
    if not args.clipboard and not args.output:
        print(codefuse.output)


if __name__ == "__main__":
    main()
