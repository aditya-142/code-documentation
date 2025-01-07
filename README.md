# Code Product Documentation Generator

This tool helps in the generation of comprehensive documentation for Python projects from a local directory or a GitHub repository. The application analyzes Python code, extracts key information (such as module docstrings, functions, and classes) & then generates detailed markdown documentation for it.

It also evaluates the quality of the generated documentation by comparing it to a reference document.

---

## Features

- **Local & GitHub Support**: Analyze Python projects from local directories or GitHub repositories.
- **Automatic Documentation Generation**: Automatically generate documentation based on your Python code's structure and content.
- **Customizable Template**: Provide a custom structure for your documentation or use the default template.
- **Documentation Evaluation**: Compare the generated documentation against a reference document and receive an evaluation report.
- **Streamlit Interface**: Interactive web-based interface built with Streamlit.

---

## Requirements

To run this project, you'll need the following:

- **Python 3.10**: python version.
- **Streamlit**: For web interface.
- **OpenAI API Key**: To access OpenAI’s GPT models for documentation generation and evaluation.
- **llama_index**: A set of tools for integrating code interpretation features into the agent.
- **GitPython**: To clone GitHub repositories.

Install the required dependencies using:

```bash
pip install -r requirements.txt
```

---

## Setup

### 1. Streamlit Secrets

To securely store your OpenAI API key, you can use **Streamlit secrets**. Create a `.streamlit/secrets.toml` file in the root directory of the project and add your OpenAI API key as follows:

```toml
[openai]
OPENAI_API_KEY = "openai_api_key"
```

### 2. Running the Application

Once the setup is complete, you can run the Streamlit application by executing:

```bash
streamlit run app.py
```

This will start the web application, and you can access it at `http://localhost:8501` in your browser.

---

## Usage

### Step 1: Input Your Project Path

Enter the path to your project. You can either:
- Provide the local directory path.
- Provide the URL to a GitHub repository (e.g., `https://github.com/username/repository`).

### Step 2: Provide a Documentation Template (Optional)

Optionally, you can provide a custom template for how you want the documentation to be structured. If you don't provide one, a default template will be used.

Example of a default template:

```markdown
# Project Overview
## Installation
## Usage
## API Reference
## Contributing
```

### Step 3: Generate Documentation

Click the "Generate Documentation" button, and the app will process your project files, extract relevant information, and generate comprehensive Markdown documentation based on the provided template.

### Step 4: Evaluate Documentation (Optional)

You can also evaluate the generated documentation against an original document. You can:
- Upload a reference document (in `.txt` or `.md` format).
- Paste the reference document directly into the app.
- Provide the path to an existing file.

After evaluation, you will receive a report comparing the original document and the generated documentation.

---

## Code Overview

### 1. **Main Functionality** (`app.py`)

- **User Input**: Accepts input for the project path (local or GitHub).
- **Project Processing**: Extracts file information using Python's `ast` module (including functions, classes, and docstrings).
- **Documentation Generation**: Uses OpenAI’s GPT-4 model to generate structured documentation in Markdown format.
- **Evaluation**: Compares generated documentation against a reference document and provides a quality evaluation.

### 2. **Agent Creation** (`agent.py`)

- Uses `llama_index` to create a custom OpenAI agent that includes code interpretation tools.
- The agent uses OpenAI’s GPT-4 model with specific configuration (temperature set to 0 for deterministic responses).
- Tools are provided by the `CodeInterpreterToolSpec`, which defines the tools available for the agent.

---

## Example

### Input: Python project directory or GitHub repository URL

- **Local Path**: `/path/to/python/project`
- **GitHub URL**: `https://github.com/username/repository`

### Output: Generated Documentation (Example)

```markdown
# Project Overview

## Installation
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`

## Usage
To run the project, execute the following command:

```bash
python main.py
```

## API Reference
### function_1
- **Description**: This function does XYZ...
- **Parameters**: 
  - `param1`: Description of param1.
- **Returns**: Description of the return value.

### function_2
- **Description**: This function does ABC...
...

## Contributing
We welcome contributions! Please fork the repository, create a pull request, and adhere to the contribution guidelines.
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## Support

If you encounter any issues or have questions, feel free to open an issue on GitHub or contact the project maintainers.

---

## Contributions

We welcome contributions to this project! If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push the branch (`git push origin feature-branch`).
5. Open a pull request.

---

Thank you for using the **Code Product Documentation Generator**! We hope it helps streamline your documentation process.
