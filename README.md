# PDFPlumberWrapper

PDFPlumberWrapper is a simple library wrapper over pdfplumber that parses PDF content to a text file. It provides both a Python API and a command-line interface (CLI) for ease of use.

## Features

- Parse PDF content to a text file using Python.
- Command-line interface for quick and easy PDF parsing.
- Simple and intuitive API.

## Installation

To install PDFPlumberWrapper, you need to clone the repository and install the dependencies using Poetry:

```bash
git clone https://github.com/inchirahjabir/pdfplumberwrapper.git
cd pdfplumberwrapper
pip install poetry
poetry install
pip install .
```
## Usage

### Using Python Code (core.py)

To parse a PDF using Python, follow these steps:

1. Import the `PDFParser` class from `pdf_parser.core`:

```bash
from pdf_parser.core import PDFParser
```

2. Initialize a `PDFParser` object with the path to the PDF file:

```bash
pdf_path = "path/to/your/pdf/file.pdf"
parser = PDFParser(pdf_path)
```

3. Optionally, specify the path to the parsed file. If not specified, the parsed file will be named based on the PDF file name with "_core_parsed.txt" appended:

```bash
parsed_file_path = "path/to/parsed_file.txt"
```

4. Call the `parse_to_file()` method to parse the PDF content and write it to the specified file:

```bash
parsed_file_path = "path/to/parsed_file.txt"
```

### Using the Command Line Interface (cli.py)

PDFPlumberWrapper also provides a CLI for parsing PDF content. To use the CLI, follow these steps:

1. Run the `cli.py` script from the command line with the path to the PDF file as the first argument:

```bash
python cli.py path/to/your/pdf/file.pdf
```

2. Optionally, specify the path to the parsed file using the `-o` or `--parsed_file_path argument`. If not specified, the parsed file will be named based on the PDF file name with "_cli_parsed.txt" appended:

```bash
pdf_path = "path/to/your/pdf/file.pdf"
parser = PDFParser(pdf_path)
```

## Unit Tests

This project includes unit tests to ensure the functionality of the core components. To run the tests, use the following command:

```bash
pytest
```

The tests are located in the `tests` directory and cover various scenarios to ensure robustness and reliability. The `tests/files` folder contains a sample PDF used for testing, and the parsed files are also generated in this folder.

## Documentation

For more detailed information, please refer to the documentation. The documentation includes:

- [Index](docs/docs/index.md)
- [Installation Guide](docs/docs/installation.md)
- [Getting Started Guide](docs/docs/getting_started.md)
- [CLI Guide](docs/docs/cli_guide.md)
- [API Reference](docs/docs/api_reference.md)
- [Contributing Guide](docs/docs/contributing_guide.md)

## Author

PDFPlumberWrapper is developed and maintained by Inchirah Jabir.