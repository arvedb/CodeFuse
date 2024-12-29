"""
CodeFuse Command-Line Interface (CLI) Module.

This module provides the command-line interface for the CodeFuse tool,
which is designed to merge multiple code files from a specified directory
into a single consolidated file. It handles parsing command-line arguments,
configuring templates for file inclusion/exclusion, and executing the merging process.
"""

import argparse
import logging
from codefuse import CodeFuse
from templates import Template, default_template
from logging_config import configure_logging  # Import the logging configuration

def setup_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="CodeFuse command line interface for merging code files into a single file."
    )
    parser.add_argument(
        "folder",
        action="store",
        default=".",
        type=str,
        help="Path to the directory to be processed",
    )
    parser.add_argument(
        "-t",
        "--template",
        action="store",
        default=default_template,
        type=Template,
        help="Template that determines which files to include or exclude",
    )
    parser.add_argument(
        "-i",
        "--include",
        nargs="+",
        default=[],
        help="List of file extensions to be included (e.g., .py .md .txt). Alternative to using template.",
    )
    parser.add_argument(
        "-e",
        "--exclude",
        nargs="+",
        default=[],
        help="List of file extensions to be excluded (e.g., .py .md .txt). Alternative to using template.",
    )
    parser.add_argument(
        "-o",
        "--output",
        nargs="?",
        const="output.txt",
        default=None,
        type=str,
        help="Path to the output file. If specified without a value, uses 'output.txt'.",
    )
    parser.add_argument(
        "-c",
        "--clipboard",
        action="store_true",
        help="Copy the output to clipboard.",
    )
    # Add log-level and log-file arguments
    parser.add_argument(
        "--log-level",
        type=str,
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Set the logging level (default: INFO).",
    )
    parser.add_argument(
        "--log-file",
        type=str,
        default=None,
        help="Optional path to a file to log messages.",
    )
    return parser

def main():
    """
    Entry point for the CodeFuse CLI.

    This function parses command-line arguments, configures logging,
    sets up the merging template, executes the merging process,
    and handles output operations such as writing to a file or copying to the clipboard.
    """
    # Set up and parse command-line arguments
    parser = setup_parser()
    args = parser.parse_args()

    # Configure logging based on the provided log level and optional log file
    configure_logging(log_level=args.log_level, log_to_file=args.log_file)

    # Obtain a logger for the CLI
    logger = logging.getLogger(__name__)
    logger.debug(f"Arguments received: {args}")

    # Determine the template to use based on provided arguments
    if args.include:
        logger.debug("Using include extensions for template.")
        template = Template(include_extensions=args.include)
    elif args.exclude:
        logger.debug("Using exclude extensions for template.")
        template = Template(exclude_extensions=args.exclude)
    else:
        logger.debug("Using default template.")
        template = default_template

    # Initialize the CodeFuse instance with the target folder and chosen template
    codefuse = CodeFuse(folder=args.folder, template=template)
    output = codefuse.generate_output()

    # Handle clipboard operation if the '-c' or '--clipboard' flag is set
    if args.clipboard:
        output.to_clipboard()

    # Handle output file writing if the '-o' or '--output' option is provided
    if args.output:
        output.to_file(path=args.output)

    # If neither clipboard nor specific output is requested, print the combined output to the console
    if not args.clipboard and not args.output:
        logger.info("Displaying merged content:")
        logger.info(output.merged_content)

if __name__ == "__main__":
    main()
