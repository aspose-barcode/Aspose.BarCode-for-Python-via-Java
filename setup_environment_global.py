import os
import subprocess


def install_dependencies():
	print("Installing dependencies from requirements.txt...")
	subprocess.check_call(['pip', 'install', '-r', 'requirements.txt'])


def check_java():
	print("Checking for Java installation...")
	try:
		# Run `java -version` and capture output
		result = subprocess.run(['java', '-version'], capture_output=True, text=True)
		if result.returncode == 0:
			# Parse the version from the stderr (Java outputs version info to stderr)
			version_output = result.stderr.splitlines()[0]
			print(f"Java version output: {version_output}")

			# Extract version number (assuming output format like 'java version "1.8.0_281"')
			if 'version' in version_output:
				version_start = version_output.find('"') + 1
				version_end = version_output.find('"', version_start)
				version = version_output[version_start:version_end]

				print(f"Java version detected: {version}")

				# Check if version is below 1.8
				major_version = float(version.split('.')[0] + '.' + version.split('.')[1])
				if major_version < 1.8:
					print("Warning: Java version is below 1.8. Please update to at least version 1.8.")

			# Run `which java` or `where java` to get installation path
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
		print("Error: Java not installed or not found in PATH.")
		print("Please install Java from https://openjdk.org/ or ensure it's added to PATH.")
		exit(1)


if __name__ == '__main__':
	check_java()
	install_dependencies()
	print("Environment setup complete!")
