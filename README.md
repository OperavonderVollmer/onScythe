# OnScythe

**OnScythe** is an automated tool designed to locate and interact with images on the screen. Using PyAutoGUI, it continuously scans for a specified image and clicks on it when found. The program allows users to save image choices and recall them later for automated interaction.

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
  pip install pyautogui
  ```
- [OperaPowerRelay](https://github.com/OperavonderVollmer/OperaPowerRelay) (Required for additional utilities)

### Manual Installation
1. Clone or download the repository.
2. Navigate to the directory containing `setup.py`:
    ```sh
    cd /path/to/OnScythe
    ```
3. Install the package in **editable mode**:
    ```sh
    pip install -e .
    ```

### Installing via pip
To install a **specific release version**, simply replace the XXXX's for the tag of the desired release:
```sh
pip install git+https://github.com/OperavonderVollmer/OnScythe.git@XXXXXXXXXX
```
This ensures you're using a stable version.

Alternatively, to install the **latest commit** from the default branch:
```sh
pip install git+https://github.com/OperavonderVollmer/OnScythe.git
```
⚠️ This may include untested changes.

## Configuration
OnScythe includes the following default constants, which can be modified by editing `OnScythe.py`:
```python
TRIES = 3  # Number of times to attempt clicking the image
WAIT_TIME = 5  # Seconds to wait between attempts
VARIANT_TIME_X = 0  # Random offset for X-coordinate
VARIANT_TIME_Y = 10  # Random offset for Y-coordinate
TRY_DELAY = 0  # Seconds to wait between tries
```
Editing these values allows for fine-tuning the script’s behavior based on user preferences.

## Usage
### Running the Program (Standalone)
Simply execute the `OnScythe.bat` file to launch OnScythe.

If dependencies are missing, install them inside a virtual environment and use `OnScytheVenv.bat` instead.

Press `Ctrl + C` to exit at any time.

### Importing as a Module
#### `watch_for`
```python
Watches the screen for an image to appear and returns the coordinates once detected.

Parameters:
  IMAGE_REFERENCE : str  -> Path to the image to look for.

Returns:
  tuple[int, int]  -> Coordinates of the image.

Raises:
  _NoImageFoundException  -> If the image is never found.
```
#### `click_and_check`
```python
Clicks on a location, waits, and checks if an image remains on the screen.

Parameters:
  x : float  -> X-coordinate of the click location.
  y : float  -> Y-coordinate of the click location.
  image_ref : str  -> Path to the image to check.
  base_wait : float  -> Base wait time before checking.
  variant_time_x : float  -> Random offset for X-coordinate.
  variant_time_y : float  -> Random offset for Y-coordinate.
  final_check : bool (default=True)  -> Perform final check for the image.

Returns:
  bool  -> True if the image is still present, False otherwise.
```
#### `click_on_sight`
```python
Clicks on an image that appears on the screen.

Parameters:
  IMAGE_REFERENCE : str  -> Path to the image to click on.
  tries : int (default=3)  -> Number of times to attempt clicking the image.
  wait_time : int (default=5)  -> Seconds to wait between attempts.
  variant_time_x : float (default=0)  -> Random offset for X-coordinate.
  variant_time_y : float (default=10)  -> Random offset for Y-coordinate.
  try_delay : int (default=0)  -> Seconds to wait between tries.

Returns:
  bool  -> True if the click was successful, False otherwise.
```

## Error Handling
- If the target image is missing, an error is displayed.
- Use `Ctrl + C` to exit safely.

## License
This project is open-source and available for modification and improvement.

