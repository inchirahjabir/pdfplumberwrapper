# CLI Guide

PDFPlumberWrapper includes a command-line interface (CLI) for parsing PDF files. This guide will help you get started with using the CLI.

## Basic Usage

To parse a PDF file and save the text to a file with the default naming convention:

```bash
python cli.py path/to/your/pdf/file.pdf
```

This will create a text file named `file_cli_parsed.txt` in the same directory as your PDF file.

## Custom Output File

You can specify a custom output file using the `-o` or `--parsed_file_path` option:

```bash
python cli.py path/to/your/pdf/file.pdf -o path/to/parsed_file.txt
```

This will save the parsed text to the specified file.

## Help Command

For more options and help, you can use the `-h` or `--help` flag:

```bash
python cli.py -h
```

This will display a help message with information on how to use the CLI.