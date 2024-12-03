#!/bin/bash

# Exit on error
set -e

# Ensure the script is executed with bash
if [ -z "$BASH_VERSION" ]; then
  echo "This script must be run with Bash."
  exit 1
fi

# Print start message
echo "Starting environment setup for Linux/macOS..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
  echo "Python3 is not installed. Please install Python3 before running this script."
  exit 1
fi

# Run the Python setup script
echo "Running setup_environment_local.py..."
python3 setup_environment_local.py

echo "Environment setup completed!"

# Print activation instructions
echo -e "\nTo activate the virtual environment, run:"
echo "source local_venv/bin/activate"
