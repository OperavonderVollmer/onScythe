# OnScythe

## Overview
OnScythe is an automated tool designed to locate and interact with images on the screen. Using PyAutoGUI, it continuously scans for a specified image and clicks on it when found. The program allows users to save image choices and recall them later for automated interaction.

## Features
- **Automated Image Detection:** Uses PyAutoGUI to find images on the screen.
- **Randomized Clicking:** Prevents detection by adding slight randomization to click locations.
- **Saved Choices:** Allows users to store image references for repeated use.
- **Customizable Attempts & Delays:** Configurable retries and wait times for robustness.

## Installation
### Prerequisites
- Python 3.x
- Required dependencies (install using pip):
  ```sh
  pip install pyautogui opencv-python
  ```
- [OperaPowerTools](https://github.com/OperavonderVollmer/OperaPowerTools) (Required for additional utilities)

## Usage
### Running the Program
Simply execute the `start.bat` file to launch OnScythe. This will activate the virtual environment and run the Python script.

### Manual Execution
If you need to run it manually, use the following commands:
```sh
# Activate the virtual environment (Windows)
.\.venv\Scripts\activate.bat

# Run the script
python OnScythe.py
```

## Configuration
### Adding Image Choices
1. When prompted, enter `0` to add a new image reference.
2. Provide a unique key and the filename (ensure it's placed inside the `assets` folder).
3. The image reference will be saved for future use.

### Running Image Detection
1. Choose an existing image reference from the list.
2. The program will start monitoring the screen for the selected image.
3. When found, it will attempt to click it within a slightly randomized boundary box.
4. If unsuccessful, it retries based on the configured attempts and delays.

## Error Handling
- If the image is not found in the `assets` folder, an error is displayed.
- If PyAutoGUI fails to detect the image on-screen, it continues waiting until found.
- Users can exit anytime with `Ctrl + C`.

## License
This project is open-source and available for modification and improvement.

