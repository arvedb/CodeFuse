from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="CodeFuse",
    version="0.1.0",
    author="Arved Bahde",
    author_email="71208362+arvedb@users.noreply.github.com",
    description="A command-line tool to combine code files into a single file.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arvedb/CodeFuse",
    packages=find_packages(),
    install_requires=[
        "argparse",
        "pyperclip",
    ],
    entry_points={
        'console_scripts': [
            'codefuse=codefuse.cli:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
