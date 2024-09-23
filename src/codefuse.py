import os

from templates import default_template, Template
from files import File


class CodeFuse:
    def __init__(self, folder: str, template: Template = default_template):
        self.folder = folder
        self.template = template
        self.all_files = self._get_all_files()
        self.included_files = [
            file
            for file in self.all_files
            if self.template.does_include(file.extension)
        ]
        self.excluded_files = [
            file
            for file in self.all_files
            if not self.template.does_include(file.extension)
        ]
        
    def _get_all_files(self) -> list[File]:
        all_files = []
        for root, _, files in os.walk(self.folder):
            for filename in files:
                all_files.append(File(os.path.join(root, filename)))
        return all_files

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
        return self._combine_files(self.included_files)

    def write_output(self, path: str):
        output_file = File(path)
        self.all_files = [
            file for file in self.all_files if file.name is not output_file.name
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
