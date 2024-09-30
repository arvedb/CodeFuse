import os

from templates import default_template, Template
from files import File
from app_data import AppData


class CodeFuse:
    def __init__(self, folder: str, template: Template = default_template, app_data: AppData = None):
        self.app_data = app_data or AppData(
            template=template,
            folder=folder
        )
        self.app_data.output = self.output

    def _combine_files(self, files: list[File]) -> str:
        if not files:
            return ""
        combined_content = []
        for file in files:
            try:
                combined_content.append("-" * 80 + f"\n\n{file.path}\n\n{file.content}")
            except Exception as e:
                raise Exception(f"Error combining file {file.path}: {e}")
        return "\n\n".join(combined_content)
    
    @property
    def output(self) -> str:
        return self._combine_files(self.app_data.included_files)

    def write_output(self, path: str):
        output_file = File(path)
        self.app_data.all_files = [
            file for file in self.app_data.all_files if file.name is not output_file.name
        ]
        try:
            with open(path, "w", encoding="utf-8") as outfile:
                outfile.write(self.output)
        except Exception as e:
            print(f"Error writing to {path}: {e}")


def main():
    codefuse = CodeFuse(".")
    print(codefuse.output)


if __name__ == "__main__":
    main()
