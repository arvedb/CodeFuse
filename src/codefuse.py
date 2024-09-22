import os

from templates import default_template, Template
from files import File

class CodeFuse:
    def __init__(self, path: str, template: Template = default_template):
        self.path = path
        self.template = template
    
    @property
    def all_files(self) -> list[File]:
        return [File(os.path.join(self.path, filename)) for filename in os.listdir(self.path)]

    @property
    def included_files(self) -> list[File]:
        return [
            file
            for file in self.all_files
            if self.template.does_include(file.extension)
        ]

    @property
    def excluded_files(self) -> list[File]:
        return [
            file
            for file in self.all_files
            if not self.template.does_include(file.extension)
        ]
    
    def _combine_files(self, files: list[File]) -> str:
        combined_content = []
        for file in files:
            combined_content.append(f"{file.path}\n\n{file.content}")
        return "-" * 80 + "\n\n" + "\n\n".join(combined_content) + "\n\n" + "-" * 80
    
    @property
    def output(self) -> str:
        return self._combine_files(self.included_files)

def main():
    codefuse = CodeFuse(".")
    print(codefuse.output)

if __name__ == "__main__":
    main()
