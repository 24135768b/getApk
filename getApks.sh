#!/bin/bash

# File containing package names, one per line
PACKAGE_FILE="packages.txt"

# Destination directory for APKs
DEST_DIR="./apks"

# Create the destination directory if it doesn't exist
mkdir -p "$DEST_DIR"

# Convert Windows line endings to Unix if necessary and read each package name
cat "$PACKAGE_FILE" | tr -d '\r' | while IFS= read -r package; do
    echo "Pulling APK for $package..."
    # Getting APK path on device
    apk_path=$(adb shell pm path "$package" | sed 's/package://g' | tr -d '\r')

    # Extract the APK filename
    apk_name=$(basename "$apk_path")

    # Pull the APK file to the destination directory
    adb pull "$apk_path" "$DEST_DIR/$apk_name"

    # Rename the APK to match the package name
    mv "$DEST_DIR/$apk_name" "$DEST_DIR/$package.apk"
done

echo "APK pull complete."
