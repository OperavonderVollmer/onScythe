from OperaPowerTools import opt
import pyautogui
import os
import json
import time

def main():
    key, path = enumerate_choices() or (None, None)
    if key is None:
        opt.print_from("OnScythe", "Something went wrong...")
    else:

        while True:
            opt.print_from("OnScythe", f"Prepared to start")
            if input ("Start? (y/n): ").lower() == "y":
                break



        try:
            click_on_sight(path)
        except Exception as e:
            print(e)

        


def enumerate_choices() -> tuple[str, str]:
    while True:
        print("\nSaved Choices\n")
        choices = choices_from_json()
        keys = list(choices.keys())  
        for idx, key in enumerate(keys, 1):
            print(f"[{idx}] {key}")
        print(f"[0] New Entry")
        decision = input(20 * "=" + "\nInput: ")

        # Handle valid number inputs
        if decision.isdigit() and 1 <= int(decision) <= len(choices):
            return keys[int(decision) - 1], choices[keys[int(decision) - 1]]
        elif decision == "0":
            if write_to_json():
                continue
            else:
                raise NoImageFoundException
        else:
            os.system("cls")
            opt.print_pretty("Invalid Choice", "=", 20)


def write_to_json() -> bool:
    choices = choices_from_json()
    os.system("cls")
    opt.print_pretty("New Entry", "=", 20)
    key = input("Key: ")
    filename = input("Filename (Make sure its in the assets folder): ")

    filename = os.path.join(os.getcwd(), "assets", filename)
    if not os.path.exists(filename):
        opt.print_pretty("File does not exist", "=", 20)
        return False

    choices[key] = filename
    JSON_PATH = os.path.join(os.getcwd(), "choices.json")
    with open(JSON_PATH, "w") as file:
        json.dump(choices, file)

    return True

def choices_from_json(verbose: bool = False) -> dict:
    JSON_PATH = os.path.join(os.getcwd(), "choices.json")
    if os.path.exists(JSON_PATH):
        print("JSON file found") if verbose else None
        with open(JSON_PATH, "r") as file:
            return json.load(file)
        
    else:
        print("No JSON file found") if verbose else None
        with open(JSON_PATH, "w") as file:
            json.dump({}, file)
        return {}

def click_on_sight(IMAGE_REFERENCE: str, tries: int = 3, wait_time: int = 5, variant_time_x: float = 0, variant_time_y: float = 10, try_delay: int = 0) -> bool:
    
    os.system("cls")

    opt.print_from("OnScythe", f"Beginning watch")

    while True:
        try:
            location = pyautogui.locateCenterOnScreen(IMAGE_REFERENCE, confidence=0.7)
        except pyautogui.ImageNotFoundException:
            location = None

        if location is not None: break       
        
        opt.print_from("OnScythe", f"Waiting...")
        time.sleep(1)

    opt.print_from("OnScythe", f"Found!")

    x, y = location
    success = False

    for _ in range(tries):
        opt.print_from("OnScythe", f"About to click...")
        opt.timed_delay(wait_time, variant_time_x, variant_time_y)

        target = opt.random_within_boundary_box(x, y, 13, 13)

        pyautogui.moveTo(target)
        pyautogui.click()

        time.sleep(0.5)
        still_there = pyautogui.locateCenterOnScreen(IMAGE_REFERENCE, confidence=0.7)
        if still_there is None: 
            success = True
            break
        
        time.sleep(try_delay)

    if success:
        opt.print_from("OnScythe", "Successfully clicked on image")
    else:
        opt.print_from("OnScythe", "Failed to click on image")

    return success

class NoImageFoundException (Exception):
    def __init__(self, message: str = None):
        super().__init__(message or "Image not found in assets folder")



if __name__ == "__main__":
    os.system("cls")
    opt.print_from("OnScythe", "Starting...")
    while True:
        try:
            opt.print_from("OnScythe", "Welcome to OnScythe. Ctrl + C to exit at any time.")
            main()
            opt.print_from("OnScythe", "Ending...")
            i = 5
            while True:
                opt.print_from("OnScythe", f"in {i}...")
                i -= 1
                if i < 1: break
                time.sleep(1)
            break
        except KeyboardInterrupt:
            break
        except NoImageFoundException as e:
            print(e)
            break
        except Exception as e:
            print(e)
            continue

    opt.print_from("OnScythe", "Shutting down...")

