import os
import subprocess
import sys


def create_and_activate_venv(venv_dir="venv"):
    """
    Creates a virtual environment in the specified directory.
    """
    print("Creating virtual environment...")
    if not os.path.exists(venv_dir):
        # Create the virtual environment
        subprocess.check_call([sys.executable, '-m', 'venv', venv_dir])
        print(f"Virtual environment created at {venv_dir}.")
    else:
        print(f"Virtual environment already exists at {venv_dir}.")

    # Determine the path to the pip executable within the virtual environment
    pip_path = os.path.join(venv_dir, 'Scripts', 'pip') if os.name == 'nt' else os.path.join(venv_dir, 'bin', 'pip')

    if not os.path.exists(pip_path):
        print("Error: pip not found in the virtual environment.")
        sys.exit(1)

    return pip_path


def install_dependencies(pip_path):
    """
    Installs dependencies from the requirements.txt file using the specified pip executable.
    """
    print("Installing dependencies from requirements.txt...")
    try:
        subprocess.check_call([pip_path, 'install', '-r', 'requirements.txt'])
        print("Dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print("Error installing dependencies.")
        print(e)
        sys.exit(1)


def check_java():
    """
    Checks if Java is installed and retrieves its version and installation path.
    """
    print("Checking for Java installation...")
    try:
        # Run `java -version` and capture output
        result = subprocess.run(['java', '-version'], capture_output=True, text=True)
        if result.returncode == 0:
            # Parse the version from stderr (Java outputs version info to stderr)
            version_output = result.stderr.splitlines()[0]
            print(f"Java version output: {version_output}")

            # Extract the version number (assuming format 'java version "1.8.0_281"')
            if 'version' in version_output:
                version_start = version_output.find('"') + 1
                version_end = version_output.find('"', version_start)
                version = version_output[version_start:version_end]

                print(f"Java version detected: {version}")

                # Check if version is below 1.8
                major_version = float(version.split('.')[0] + '.' + version.split('.')[1])
                if major_version < 1.8:
                    print("Warning: Java version is below 1.8. Please update to at least version 1.8.")

            # Get the Java installation path
            path_result = subprocess.run(['where' if os.name == 'nt' else 'which', 'java'], capture_output=True,
                                         text=True)
            if path_result.returncode == 0:
                java_path = path_result.stdout.strip()
                print(f"Java installation path: {java_path}")
            else:
                print("Unable to locate Java installation path.")

        else:
            raise Exception("Java not found.")
    except Exception:
        print("Error: Java not installed or not found in PATH.")
        print("Please install Java from https://openjdk.org/ or ensure it's added to PATH.")
        sys.exit(1)


if __name__ == '__main__':
    check_java()
    venv_dir = "venv"  # Directory for the virtual environment
    pip_path = create_and_activate_venv(venv_dir)
    install_dependencies(pip_path)
    print("Environment setup complete!")
