import subprocess
import os

# Path to the file containing package names
package_file = 'packages.txt'

# Destination directory for the APKs
dest_dir = './apks'

# Create the destination directory if it doesn't exist
subprocess.run(['mkdir', '-p', dest_dir], check=True)

# Read package names from the file
with open(package_file, 'r') as file:
    for package_name in file:
        package_name = package_name.strip()
        print(f'Pulling APK for {package_name}...')
        
        # Get APK path on device
        apk_path_process = subprocess.run(['adb', 'shell', 'pm', 'path', package_name], capture_output=True, text=True)
        
        # Extract the first APK path
        apk_paths = apk_path_process.stdout.split('\n')
        for line in apk_paths:
            if line.startswith('package:'):
                apk_path = line.split(':')[1].strip()
                break
        
        # Destination file path
        dest_file_path = os.path.join(dest_dir, f"{package_name}.apk")
        
        # Pull the APK file to the specified destination
        try:
            subprocess.run(['adb', 'pull', apk_path, dest_file_path], check=True)
            print(f'Successfully pulled {package_name} to {dest_file_path}')
        except subprocess.CalledProcessError as e:
            print(f'Failed to pull APK for {package_name}: {e}')

print('APK pull complete.')
