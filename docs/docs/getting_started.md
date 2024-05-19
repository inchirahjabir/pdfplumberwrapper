# Getting Started Guide

PDFPlumberWrapper provides two methods for parsing PDF content: using the Python code directly or through the command-line interface (CLI).

## Using Python Code (core.py)

To parse PDF content using Python code, follow these steps:

1. Import the `PDFParser` class from `pdf_parser.core`.
   
```python
from pdf_parser.core import PDFParser
```

2. Initialize a `PDFParser` object with the path to the PDF file.

```bash
pdf_path = "path/to/your/pdf/file.pdf"
parser = PDFParser(pdf_path)
```

3. Optionally, specify the path to the parsed file. If not specified, the parsed file will be named based on the PDF file name with "_core_parsed.txt" appended.

```bash
parsed_file_path = "path/to/parsed_file.txt"
```

4. Call the `parse_to_file()` method to parse the PDF content and write it to the specified file.

```bash
parser.parse_to_file(parsed_file_path)
```

## Using the Command-Line Interface (CLI) (cli.py)

PDFPlumberWrapper also provides a command-line interface for parsing PDF content. To use the CLI, follow these steps:

1. Run the `cli.py` script from the command line with the path to the PDF file as the first argument.
   
```bash
python cli.py path/to/your/pdf/file.pdf
```

2. Optionally, specify the path to the parsed file using the `-o` or `--parsed_file_path` argument. If not specified, the parsed file will be named based on the PDF file name with "_cli_parsed.txt" appended.

```bash
python cli.py path/to/your/pdf/file.pdf -o path/to/parsed_file.txt
```

## Next Steps

For more advanced usage and customization options, refer to the [API Reference](api_reference.md) and [CLI Guide](cli_guide.md). If you encounter any issues or have questions, don't hesitate to reach out to the project's GitHub repository for support.