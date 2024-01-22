#!/bin/bash

SCRIPT_NAME="flowcleanser"

SOURCE_SCRIPT="./$SCRIPT_NAME"

DEST_DIR="/usr/local/bin"

echo "Checking for required dependencies..."
if ! command -v curl &> /dev/null; then
    echo "Error: curl is not installed. Please install curl and try again."
    exit 1
fi

if ! command -v jq &> /dev/null; then
    echo "Error: jq is not installed. Please install jq and try again."
    exit 1
fi

echo "Installing the script..."
if cp "$SOURCE_SCRIPT" "$DEST_DIR"; then
    echo "Script successfully installed to $DEST_DIR"
else
    echo "Error installing the script."
    exit 1
fi

chmod +x "$DEST_DIR/$SCRIPT_NAME"

echo "Installation complete. You can now run the script with '$SCRIPT_NAME'."
