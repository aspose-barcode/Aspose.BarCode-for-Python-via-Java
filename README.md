# Barcode Generation & Recognition via Python

[Product Page](https://products.aspose.com/barcode/python-java) | [Docs](https://docs.aspose.com/barcode/pythonjava/) | [Demos](https://products.aspose.app/barcode/family) | [API Reference](https://apireference.aspose.com/barcode/python) | [Examples](https://github.com/aspose-barcode/Aspose.BarCode-for-Python-via-Java/tree/master/src/examples) | [Blog](https://blog.aspose.com/category/barcode/) | [Search](https://search.aspose.com/) | [Free Support](https://forum.aspose.com/c/barcode) | [Temporary License](https://purchase.aspose.com/temporary-license)

Aspose.BarCode for Python via Java is a robust and reliable barcode generation and recognition component, written in Python and Java. It allows developers to quickly and easily add barcode creation and scanning functionality to their Python applications.

---

<p align="center">
    <a title="Download complete Aspose.BarCode for Python via Java Examples source code" href="https://github.com/aspose-barcode/Aspose.BarCode-for-Python-via-Java/archive/refs/heads/master.zip">
    <img src="https://raw.github.com/AsposeExamples/java-examples-dashboard/master/images/downloadZip-Button-Large.png" alt="Download Aspose.BarCode for Python via Java" />
    </a>
</p>
---

## General Barcode Features

- Supports most established barcode standards and barcode specifications.
- Ability to read & export barcodes in multiple image formats, including BMP, GIF, JPEG & PNG.
- Provides full control over barcode images including background color, bar color, image quality, rotation angle, x-dimension, resolution, and more.
- Complete control over barcode captions including caption font, background color, foreground color, alignment, and location.
- Support for checksum.
- Support for X-dimension & Y-dimension for 2D barcodes.
- Support for Wide to Narrow Ratio for supported symbologies.
- Support for DataMatrix barcode with X12, EDIFACT & Base 256 encoding.

---

## Barcode Recognition Features

- Can read most common 1D and 2D barcodes from an image at any angle.
- Specify an area in the image to scan the barcode.
- Get region information for the barcodes recognized in the image.

---

## Barcode Imaging Features

- Manipulate the barcode's image borders, border color, style, margins, and width.
- Rotate barcode images to any degree.
- Set anti-aliasing for barcode images.
- Manage barcode image margins.
- Customize image resolution.
- Set size in inches or millimeters.
- Auto size barcode images.

---

## Barcode Symbologies

### Numeric Only
EAN13, EAN8, UPCA, UPCE, ISBN, ISMN, ISSN, Interleaved2of5, Standard2of5, MSI, Code11, Codabar, Postnet, Planet, EAN14 (SCC14), SSCC18, ITF14, IATA 2 of 5, DatabarOmniDirectional, DatabarStackedOmniDirectional, DatabarExpandedStacked, DatabarStacked, DatabarLimited, DatabarTruncated.

### Alpha-Numeric
GS1Code128, Code128, Code39 Extended, Code39 Standard, Code93 Extended, Code93 Standard, Australia Post, Italian Post 25, Matrix 2 of 5, DatabarExpanded, PatchCode.

### 2D Symbologies
PDF417, DataMatrix, Aztec, QR, MicroQR, GS1DataMatrix, Code16K, CompactPDF417, Swiss QR (QR Bill).

---

## Read Barcodes From

- **Images:** JPEG, TIFF, PNG, BMP.

---

## Save Barcode Labels As

- **Images:** JPEG, TIFF, PNG, BMP.



---

## Project Structure

This project provides examples and tools for working with **Aspose.BarCode for Python via Java**. 
Below is a description of the main directories and their purposes.

| Directory               | Description                                                                 |
| ----------------------- | --------------------------------------------------------------------------- |
| [docs](docs)            | Documentation files related to the project (if available).                 |
| [examples](examples)    | A collection of Python examples to demonstrate the product features.       |
| ├── barcode_parameters  | Examples of configuring and working with barcode parameters.               |
| ├── generate_barcode    | Examples of generating barcodes using various configurations.              |
| ├── read_barcode        | Examples of reading barcodes from different types of input.                |
| ├── utilities           | Helper scripts and utilities for barcode processing.                      |
| [local_venv](local_venv)| Virtual environment directory (created by `setup_environment_local.py`).   |
| [resources](resources)  | Contains additional resources used in examples (input files, output files).|
| ├── generated           | Directory where generated barcodes are saved.                             |
| ├── input               | Input files used for examples (e.g., images with barcodes).               |
| ├── license             | Placeholder for license files or information.                             |
| .gitignore              | Specifies intentionally untracked files to ignore in the project.         |
| README.md               | Project overview and instructions for setup and usage.                    |
| requirements.txt        | List of dependencies required for the project.                            |
| setup_environment_global.py | Script for setting up the environment globally.                       |
| setup_environment_local.py  | Script for setting up the environment in a virtual environment.        |


---

## Get Started with Aspose.BarCode for Python via Java

1. **Install Python**  
   Ensure you have Python installed, version **>= 3.7**. You can download it from the official [Python website](https://www.python.org/).

2. **Install Dependencies**  
   You can install the required dependencies either globally or in a local repository. Choose the appropriate method depending on your needs:

   - **Install Dependencies Globally**  
     To install dependencies globally, run the following script:
     ```bash
     python setup_environment_global.py
     ```
     This will install all required packages into the global Python environment.

   - **Install Dependencies Locally**  
     To isolate dependencies for this project, use a local virtual environment. Run the following script:
     ```bash
     python setup_environment_local.py
     ```
     This will create a directory named `local_venv` in your project structure and install all required dependencies into it.  

     After running the script, activate the virtual environment:  
     ```bash
     local_venv\Scripts\activate  # On Windows
     source local_venv/bin/activate  # On Linux/macOS
     ```

   - **Install the Library with PIP**  
     You can also install the `Aspose.BarCode` library directly using `pip` from [PyPI](https://pypi.org/project/aspose-barcode-for-python-via-java/):  
     ```bash
     pip install aspose-barcode-for-python-via-java
     ```
     To install a specific version of the library in the global environment:
     ```bash
     pip install aspose-barcode-for-python-via-java==24.11.0
     ```

     To install a specific version in a local directory:
     ```bash
     pip install aspose-barcode-for-python-via-java==24.11.0 --upgrade -t ./local_venv
     ```

3. **Explore Examples**  
   Explore example usage of the library in the official [GitHub Examples Repository](https://github.com/aspose-barcode/Aspose.BarCode-for-Python-via-Java/tree/master/examples).
---

[Product Page](https://products.aspose.com/barcode/python-java) | [Docs](https://docs.aspose.com/barcode/pythonjava/) | [Demos](https://products.aspose.app/barcode/family) | [API Reference](https://apireference.aspose.com/barcode/python) | [Examples](https://github.com/aspose-barcode/Aspose.BarCode-for-Python-via-Java/tree/master/src/examples) | [Blog](https://blog.aspose.com/category/barcode/) | [Search](https://search.aspose.com/) | [Free Support](https://forum.aspose.com/c/barcode) | [Temporary License](https://purchase.aspose.com/temporary-license)
