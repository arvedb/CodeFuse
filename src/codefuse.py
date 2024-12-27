
from templates import default_template, Template
from app_data import AppData
from output_data import Output


class CodeFuse:
    """
    CodeFuse orchestrates scanning files via AppData
    and generating an Output object with the merged content.
    """
    def __init__(
        self,
        folder: str,
        template: Template = default_template
    ):
        self.app_data = AppData(folder=folder, template=template)

    def _combine_files(self) -> str:
        """
        Combines the content of all included files into a single string,
        along with a simple delimiter (e.g., 80 dashes).
        """
        included_files = self.app_data.included_files
        if not included_files:
            return ""

        combined_content = []
        for file_obj in included_files:
            combined_content.append("-" * 80)         # Delimiter
            combined_content.append(file_obj.path)    # Show file path
            combined_content.append(file_obj.content) # The file's actual content
        return "\n\n".join(combined_content)

    def generate_output(self) -> Output:
        """
        Creates and returns an Output object containing the merged file contents
        and any additional metadata (e.g., how many files were merged).
        """
        content = self._combine_files()
        return Output(merged_content=content)


def main():
    codefuse = CodeFuse(".")
    output = codefuse.generate_output()
    print(output.merged_content)


if __name__ == "__main__":
    main()
