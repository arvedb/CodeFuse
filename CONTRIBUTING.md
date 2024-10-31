# Contributing to CodeFuse

I welcome contributions from the community! To ensure a smooth and efficient collaboration process, please adhere to the following **Contribution Standards** designed to maintain high code quality and consistency.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Requesting Features](#requesting-features)
  - [Suggesting Improvements](#suggesting-improvements)
- [Code Style Guidelines](#code-style-guidelines)
- [Testing](#testing)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)
- [Additional Resources](#additional-resources)

### Code of Conduct

Please read and follow our [Code of Conduct](CODE_OF_CONDUCT.md) to ensure a welcoming and respectful community for everyone.

### How to Contribute

#### Reporting Bugs

If you find a bug in CodeFuse, please follow these steps:

1. **Check Existing Issues:**  
   Ensure that the bug hasn't already been reported by searching [existing issues](https://github.com/arvedb/CodeFuse/issues).

2. **Open a New Issue:**  
   If the bug is new, open a [Bug Report](https://github.com/arvedb/CodeFuse/issues/new?assignees=&labels=bug&template=bug_report.md&title=) and provide the following information:
   
   - **Description:** A clear and concise description of what the bug is.
   - **To Reproduce:** Steps to reproduce the behavior.
   - **Expected Behavior:** A clear and concise description of what you expected to happen.
   - **Screenshots:** If applicable, add screenshots to help explain your problem.
   - **Environment:** Information about your system (OS, Python version, etc.).
   - **Additional Context:** Any other context about the problem.

#### Requesting Features

To request new features, please:

1. **Search Existing Issues:**  
   Check if the feature has already been requested by searching [existing issues](https://github.com/arvedb/CodeFuse/issues).

2. **Open a New Feature Request:**  
   Provide a detailed description by opening a [Feature Request](https://github.com/arvedb/CodeFuse/issues/new?assignees=&labels=feature%20request&template=feature_request.md&title=).

#### Suggesting Improvements

For suggestions on improving CodeFuse:

1. **Open an Improvement Request:**  
   Use the [Refactor / Improvement Request](https://github.com/arvedb/CodeFuse/issues/new?assignees=&labels=refactor%20improvement%20request&template=refactor_improvement_request.md&title=) template to propose enhancements.

### Code Style Guidelines

Maintaining a consistent code style is vital for readability and maintainability. Please adhere to the following guidelines:

- **Follow PEP 8:**  
  Adhere to [PEP 8](https://pep8.org/), the Python style guide.

- **Use Type Hints:**  
  Utilize type annotations for better code clarity and to aid tools like linters and IDEs.

- **Consistent Naming Conventions:**  
  - Use `snake_case` for functions and variables.
  - Use `CamelCase` for classes.
  - Constants should be in `UPPER_SNAKE_CASE`.

- **Documentation:**  
  - Write clear and concise docstrings for all modules, classes, and functions using [Google Style](https://google.github.io/styleguide/pyguide.html) or [NumPy Style](https://numpydoc.readthedocs.io/en/latest/format.html).
  - Ensure all public APIs are well-documented.

- **Modular Code:**  
  - Keep functions and classes focused and limited to single responsibilities.
  - Avoid large, monolithic functions; break them down into smaller, reusable components.

### Testing

Comprehensive testing ensures the reliability and stability of CodeFuse.

- **Write Unit Tests:**  
  - Cover all critical functionalities.
  - Use [pytest](https://docs.pytest.org/en/stable/) as the testing framework.

- **Test Coverage:**  
  - Aim for at least **80%** test coverage.
  - Use tools like [coverage.py](https://coverage.readthedocs.io/en/coverage-5.5/) to measure coverage.

- **Continuous Integration (CI):**  
  - Ensure that all tests pass before merging any pull requests.
  - GitHub Actions is configured to run tests on each push and pull request.

### Commit Guidelines

Clear and meaningful commit messages are essential for tracking changes and understanding the project history.

- **Follow Conventional Commits:**  
  Structure your commit messages as follows:

  ```
  <type>[optional scope]: <description>

  [optional body]

  [optional footer(s)]
  ```

  **Types:**
  
  - `feat`: A new feature
  - `fix`: A bug fix
  - `docs`: Documentation only changes
  - `style`: Changes that do not affect the meaning of the code (white-space, formatting, etc.)
  - `refactor`: A code change that neither fixes a bug nor adds a feature
  - `test`: Adding missing tests or correcting existing tests
  - `chore`: Changes to the build process or auxiliary tools and libraries

  **Example:**
  
  ```
  feat(cli): add support for custom templates
  ```

### Pull Request Process

To ensure smooth and efficient code reviews, please follow this process when submitting pull requests (PRs):

1. **Fork the Repository:**  
   Create a personal fork of the project repository.

2. **Create a New Branch:**  
   Branch off from `main` using a descriptive name.
   
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Your Changes:**  
   Implement your feature or fix, adhering to the code style guidelines.

4. **Write Tests:**  
   Add or update tests to cover your changes.

5. **Run Tests Locally:**  
   Ensure all tests pass before submitting.
   
   ```bash
   pytest
   ```

6. **Commit Your Changes:**  
   Use clear and descriptive commit messages following the commit guidelines.
   
   ```bash
   git commit -m "feat(cli): add support for custom templates"
   ```

7. **Push to Your Fork:**  
   ```bash
   git push origin feature/your-feature-name
   ```

8. **Open a Pull Request:**  
   - Navigate to the original repository.
   - Click on "New Pull Request."
   - Provide a clear description of your changes, referencing any relevant issues.

9. **Address Feedback:**  
   Be responsive to review comments and make necessary adjustments.

10. **Merge:**  
    Once approved, your PR can be merged by the project maintainers.

### Additional Resources

- **Issue Templates:**  
  Utilize the predefined issue templates for reporting bugs and requesting features.

- **Documentation:**  
  Refer to the [CodeFuse Documentation](https://github.com/arvedb/CodeFuse/wiki) for detailed usage instructions and API references.

- **Code of Conduct:**  
  Adhere to the [Code of Conduct](/CODE_OF_CONDUCT.md) to maintain a respectful and inclusive community.