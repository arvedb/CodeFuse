import os


class CodeFuse:
    def __init__(self, path, included_files=None):
        self.path = path
        self.included_files = included_files if included_files is not None else []

    @property
    def file_list(self):
        return os.listdir(self.path)

    @property
    def file_list_filtered(self):
        return [file for file in self.file_list if file.endswith('.py')]

    def _get_file_content(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return file.read()

