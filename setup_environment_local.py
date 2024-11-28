import os
import subprocess
import sys


def create_and_activate_venv(venv_dir="local_venv"):
    """
    Creates a virtual environment and ensures pip is available.
    """
    print("Creating virtual environment...")
    if not os.path.exists(venv_dir):
        # Create the virtual environment
        subprocess.check_call([sys.executable, '-m', 'venv', venv_dir])
        print(f"Virtual environment created at {venv_dir}.")
    else:
        print(f"Virtual environment already exists at {venv_dir}.")

    # Determine the path to pip
    pip_path = os.path.join(venv_dir, 'Scripts', 'pip') if os.name == 'nt' else os.path.join(venv_dir, 'bin', 'pip')
    print(f"Looking for pip at: {pip_path}")

    # Check if pip exists
    if not os.path.exists(pip_path):
        print("pip not found. Attempting to install pip...")
        subprocess.check_call([sys.executable, '-m', 'ensurepip'])
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])

    if not os.path.exists(pip_path):
        print("Error: pip installation failed.")
        sys.exit(1)

    return pip_path
