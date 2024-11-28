import os
import subprocess
import sys


def create_and_activate_venv(venv_dir="local_venv"):
    """
    Creates a virtual environment and ensures pip is available within it.
    """
    print("Step 1: Creating virtual environment...")
    if not os.path.exists(venv_dir):
        try:
            subprocess.check_call([sys.executable, '-m', 'venv', venv_dir])
            print(f"Virtual environment created at {venv_dir}.")
        except subprocess.CalledProcessError as e:
            print(f"Error creating virtual environment: {e}")
            sys.exit(1)
    else:
        print(f"Virtual environment already exists at {venv_dir}.")

    # Define the paths to python and pip in the virtual environment
    python_executable = os.path.join(venv_dir, 'Scripts', 'python') if os.name == 'nt' else os.path.join(venv_dir, 'bin', 'python')
    pip_executable = os.path.join(venv_dir, 'Scripts', 'pip') if os.name == 'nt' else os.path.join(venv_dir, 'bin', 'pip')

    print(f"Using Python at: {python_executable}")
    print(f"Using pip at: {pip_executable}")

    # Check if pip exists and install it if missing
    if not os.path.exists(pip_executable):
        print("pip not found. Installing pip in the virtual environment...")
        try:
            subprocess.check_call([python_executable, '-m', 'ensurepip'])
            subprocess.check_call([python_executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
        except subprocess.CalledProcessError as e:
            print(f"Error installing or upgrading pip: {e}")
            sys.exit(1)

    print("Step 2: Virtual environment is ready.")
    return python_executable, pip_executable


def install_dependencies(pip_executable):
    """
    Installs dependencies from the requirements.txt file using the specified pip executable.
    """
    print("Step 3: Installing dependencies...")
    try:
        subprocess.check_call([pip_executable, 'install', '-r', 'requirements.txt'])
        print("Dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        sys.exit(1)


def check_java():
    """
    Checks if Java is installed and retrieves its version and installation path.
    """
    print("Step 0: Checking for Java installation...")
    try:
        result = subprocess.run(['java', '-version'], capture_output=True, text=True)
        if result.returncode == 0:
            version_output = result.stderr.splitlines()[0]
            print(f"Java version output: {version_output}")

            if 'version' in version_output:
                version_start = version_output.find('"') + 1
                version_end = version_output.find('"', version_start)
                version = version_output[version_start:version_end]

                print(f"Java version detected: {version}")

            path_result = subprocess.run(['where' if os.name == 'nt' else 'which', 'java'], capture_output=True,
                                         text=True)
            if path_result.returncode == 0:
                java_path = path_result.stdout.strip()
                print(f"Java installation path: {java_path}")
            else:
                print("Unable to locate Java installation path.")
        else:
            raise Exception("Java not found.")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    print("Starting environment setup...")
    check_java()
    venv_dir = "local_venv"  # Directory for the virtual environment
    python_executable, pip_executable = create_and_activate_venv(venv_dir)
    install_dependencies(pip_executable)
    print("Environment setup complete!")
