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