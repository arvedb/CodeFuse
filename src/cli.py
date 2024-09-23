import argparse
from codefuse import CodeFuse
from templates import Template, default_template


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
    return parser

    
def main():
    parser = setup_parser()
    args = parser.parse_args()

    if args.include:
        template = Template(include_extensions=args.include)
    elif args.exclude:
        template = Template(exclude_extensions=args.exclude)
    else:
        template = default_template

    codefuse = CodeFuse(folder=args.folder, template=template)
    
    if args.clipboard:
        import pyperclip
        pyperclip.copy(codefuse.output)
        print("Combined code has been copied to the clipboard.")
        
    if args.output:
        codefuse.write_output(path=args.output)
        print(f"Combined code has been written to {args.output}")


if __name__ == "__main__":
    main()
