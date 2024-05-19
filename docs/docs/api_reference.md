# API Reference

## PDFParser Class

The `PDFParser` class provides methods to parse PDF content and write it to a text file.

### Initialization

```bash
PDFParser(pdf_path: Union[str, Path])
```

- `pdf_path` (Union[str, Path]): The path to the PDF file to be parsed.

### Methods

`parse_to_file(parsed_file_path: Union[str, Path] = None) -> Union[str, Path]`

Parses the PDF content and writes it to a text file.

- `parsed_file_path` (Union[str, Path], optional): Path to the parsed text file. If not specified, the parsed file will have the same name as the PDF file with "_core_parsed.txt" appended.
- Returns: The path to the parsed text file.

#### Example

```bash
from pdf_parser.core import PDFParser

pdf_path = "path/to/your/pdf/file.pdf"
parser = PDFParser(pdf_path)
parsed_file_path = parser.parse_to_file()
```