import os

from templates.templates import DefaultTemplate


class CodeFuse:
    def __init__(self, path, template: DefaultTemplate = DefaultTemplate):
        self.path = path
        self.template = template
    
    @property
    def all_files(self) -> list[str]:
        return os.listdir(self.path)

    @property
    def included_files(self) -> list[str]:
        filtered_files = [
            file
            for file in self.all_files
            if os.path.splitext(file)[1] in self.template.included_files
        ]
        return filtered_files

    @property
    def excluded_files(self) -> list[str]:
        filtered_files = [
            file
            for file in self.all_files
            if os.path.splitext(file)[1] not in self.template.included_files
        ]
        return filtered_files

    def _get_file_content(self, file_path: str) -> str:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
