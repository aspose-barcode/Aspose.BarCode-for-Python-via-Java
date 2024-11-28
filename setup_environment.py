import os
import subprocess

def install_dependencies():
    print("Installing dependencies from requirements.txt...")
    subprocess.check_call(['pip', 'install', '-r', 'requirements.txt'])

def check_java():
    print("Checking for Java installation...")
    try:
        result = subprocess.run(['java', '-version'], capture_output=True, text=True)
        if result.returncode == 0:
            print("Java is installed.")
        else:
            raise Exception("Java not found.")
    except Exception as e:
        print("Error: Java not installed or not found in PATH.")
        print("Please install Java from https://openjdk.org/ or ensure it's added to PATH.")
        exit(1)

if __name__ == '__main__':
    check_java()
    install_dependencies()
    print("Environment setup complete!")
