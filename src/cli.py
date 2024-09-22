import argparse
from codefuse import CodeFuse
from templates import Template, default_template

def setup_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="CodeFuse command line interface for merging code files into a single file."
    )
    parser.add_argument(
        "path",
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
        action="store_true",
        help="List of file extensions to be included (e.g., .py .md .txt). Alternative to using template.",
    )
    parser.add_argument(
        "-e",
        "--exclude",
        action="store_true",
        help="List of file extensions to be excluded (e.g., .py .md .txt). Alternative to using template.",
    )
    parser.add_argument(
        "-o",
        "--output",
        action="store",
        default="output.txt",
        type=str,
        help="Path to the output file.",
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

    codefuse = CodeFuse(args.path, template=template)
    combined_content = codefuse.output

    with open(args.output, "w", encoding="utf-8") as outfile:
        outfile.write(combined_content)

    print(f"Combined code has been written to {args.output}")

if __name__ == "__main__":
    main()