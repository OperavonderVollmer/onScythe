from OperaPowerRelay import opr
import pyautogui
import os
import json
import time

# CONSTANTS, if you want to change them

TRIES = 3
WAIT_TIME = 5
VARIANT_TIME_X = 0
VARIANT_TIME_Y = 10
TRY_DELAY = 0

def _main():
    key, path = _enumerate_choices() or (None, None)
    if key is None:
        opr.print_from("OnScythe", "Something went wrong...")
        return
    
    while True:
        opr.print_from("OnScythe", f"Prepared to start")
        if input ("Start? (y/n): ").lower() == "y":
            break
    try:
        os.system("cls")
        click_on_sight(IMAGE_REFERENCE=path, tries=TRIES, wait_time=WAIT_TIME, variant_time_x=VARIANT_TIME_X, variant_time_y=VARIANT_TIME_Y, try_delay=TRY_DELAY)
    except Exception as e:
        print(e)

def _enumerate_choices() -> tuple[str, str]:
    while True:
        print("\nSaved Choices\n")
        choices = _choices_from_json()
        keys = list(choices.keys())  
        for idx, key in enumerate(keys, 1):
            print(f"[{idx}] {key}")
        print(f"[0] New Entry")
        decision = input(20 * "=" + "\nInput: ")

        # Handle valid number inputs
        if decision.isdigit() and 1 <= int(decision) <= len(choices):
            return keys[int(decision) - 1], choices[keys[int(decision) - 1]]
        elif decision == "0":
            if _write_to_json():
                continue
            else:
                raise _NoImageFoundException
        else:
            os.system("cls")
            opr.print_pretty("Invalid Choice", "=", 20)


def _write_to_json() -> bool:
    choices = _choices_from_json()
    os.system("cls")
    opr.print_pretty("New Entry", "=", 20)
    key = input("Key: ")
    filename = input("Filename (Make sure its in the assets folder): ")

    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", filename)
    if not os.path.exists(filename):
        opr.print_pretty("File does not exist", "=", 20)
        return False

    choices[key] = filename
    JSON_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "choices.json")
    with open(JSON_PATH, "w") as file:
        json.dump(choices, file)

    os.getcwd

    return True

def _choices_from_json(verbose: bool = False) -> dict:
    JSON_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "choices.json")
    if os.path.exists(JSON_PATH):
        print("JSON file found") if verbose else None
        with open(JSON_PATH, "r") as file:
            return json.load(file)
        
    else:
        print("No JSON file found") if verbose else None
        with open(JSON_PATH, "w") as file:
            json.dump({}, file)
        return {}


def watch_for(IMAGE_REFERENCE: str) -> tuple[int, int]:
    """
    Watches the screen for an image to appear and returns the coordinates of it once it does.

    Parameters
    ----------
    IMAGE_REFERENCE : str
        The path to the image to look for.

    Returns
    -------
    tuple[int, int]
        The coordinates of the image once it appears on the screen.

    Raises
    ------
    _NoImageFoundException
        If the image is never found on the screen.
    """
    return opr.stubborn_call(IMAGE_REFERENCE, func=pyautogui.locateCenterOnScreen, stubborn=True, wait_time=0.5, whitelist=[pyautogui.ImageNotFoundException])

def click_and_check(x: float, y: float, image_ref: str, base_wait: float, variant_time_x: float, variant_time_y: float, centered_click: bool = False, final_check: bool = True) -> bool:
    """
    Clicks on a location on the screen, waits a bit, and then checks if an image is still on the screen.

    Parameters
    ----------
    x : float
        The x-coordinate of the location to click.
    y : float
        The y-coordinate of the location to click.
    image_ref : str
        The path to the image to check for.
    base_wait : float
        The base amount of time to wait before checking for the image.
    variant_time_x : float
        The amount of time to randomly add to the x-coordinate of the click.
    variant_time_y : float
        The amount of time to randomly add to the y-coordinate of the click.
    final_check : bool, optional
        Whether to do a final check for the image after waiting. Defaults to True.

    Returns
    -------
    bool
        True if the image was still on the screen after waiting, False otherwise.
    """
    opr.print_from("OnScythe - click_and_check", f"About to click...")

    opr.timed_delay(base_wait, variant_time_x, variant_time_y)

    target = opr.random_within_boundary_box(x, y, 13, 13, centered_click)

    pyautogui.moveTo(target)
    pyautogui.click()

    opr.print_from("OnScythe - click_and_check", "Clicked!")

    time.sleep(0.5)

    if not final_check:
        return False
    
    try:
        s = pyautogui.locateCenterOnScreen(image_ref) is not None
        if s:
            opr.print_from("OnScythe - click and check", "Image still there!")
        return s 
    except pyautogui.ImageNotFoundException:
        opr.print_from("OnScythe - click and check", "Image no longer there!")
        return False

def click_on_sight(IMAGE_REFERENCE: str, tries: int = 3, wait_time: int = 5, variant_time_x: float = 0, variant_time_y: float = 10, try_delay: int = 0) -> bool:
    
    """
    Clicks on an image that appears on the screen.

    Parameters
    ----------
    IMAGE_REFERENCE : str
        The path to the image to click on.
    tries : int, optional
        The number of times to attempt to click on the image. Defaults to 3.
    wait_time : int, optional
        The number of seconds to wait between attempts. Defaults to 5.
    variant_time_x : float, optional
        The amount of time to randomly add to the x-coordinate of the click.
        Defaults to 0.
    variant_time_y : float, optional
        The amount of time to randomly add to the y-coordinate of the click.
        Defaults to 10.
    try_delay : int, optional
        The number of seconds to wait between tries. Defaults to 0.

    Returns
    -------
    bool
        True if the click was successful, False otherwise.
    """
    

    opr.print_from("OnScythe - click_on_sight", f"Beginning watch")    

    location = watch_for(IMAGE_REFERENCE)

    opr.print_from("OnScythe - click_on_sight", f"Found!")

    x, y = location
    not_found = False


# Negating the result since true = found
    not_found = not opr.hammer_call(x, y, IMAGE_REFERENCE, variant_time_x, variant_time_y, wait_time, func=click_and_check, try_count=tries, stop_at= lambda result:result, stop_if=False, wait_time = try_delay)   


    if not_found:
        opr.print_from("OnScythe - click_on_sight", "Successfully clicked on image")
    else:
        opr.print_from("OnScythe - click_on_sight", "Failed to click on image")

    return not_found

class _NoImageFoundException (Exception):
    def __init__(self, message: str = None):
        super().__init__(message or "Image not found in assets folder")



if __name__ == "__main__":
    os.system("cls")
    opr.print_from("OnScythe", "Starting...")
    while True:
        try:
            opr.print_from("OnScythe", "Welcome to OnScythe. Ctrl + C to exit at any time.")
            _main()
            opr.print_from("OnScythe", "Ending...")
            i = 3
            while True:
                opr.print_from("OnScythe", f"in {i}...")
                i -= 1
                if i < 1: break
                time.sleep(1)
            break
        except KeyboardInterrupt:
            break
        except _NoImageFoundException as e:
            print(e)
            break
        except Exception as e:
            print(e)
            continue

    opr.print_from("OnScythe", "Shutting down...")

