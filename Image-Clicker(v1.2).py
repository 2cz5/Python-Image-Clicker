# | Made by 2cz5 | https://github.com/2cz5 | Discord:2cz5 (for questions etc..)

import os
import cv2
import numpy as np
import pyautogui
import keyboard
import time

# Function to minimize the command prompt window (Windows-specific)
def minimize_cmd_window():
    try:
        import win32gui
        import win32con
        hwnd = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
    except ImportError:
        pass  # If win32gui module is not available, ignore and proceed

# Function to search for images on the screen and click on them if found
def search_and_click(images, threshold=0.8, click_delay=1, killswitch_key='q'):
    # Set the template matching method
    method = cv2.TM_CCOEFF_NORMED
    
    while True:
        minimize_cmd_window()  # Minimize the command prompt window
        
        # Check if the killswitch key is pressed
        if keyboard.is_pressed(killswitch_key):
            print("Killswitch activated. Exiting the loop.")
            break

        # Capture the screen image
        screenshot = pyautogui.screenshot()
        screen_np = np.array(screenshot)
        screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_RGB2GRAY)

        # Iterate through each image in the database
        for image_path in images:
            if not os.path.exists(image_path):
                print(f"Error: Image not found at '{image_path}'")
                continue  # Skip to the next image if the file doesn't exist

            # Load the image from the database
            template = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

            # Perform template matching
            result = cv2.matchTemplate(screen_gray, template, method)

            # Get the location of matches above a specified threshold
            loc = np.where(result >= threshold)

            # Click on the matched locations
            if loc[0].size > 0:
                for pt in zip(*loc[::-1]):
                    # Calculate the center of the matched template
                    x, y = pt[0] + template.shape[1] // 2, pt[1] + template.shape[0] // 2

                    # Click on the center of the matched template
                    pyautogui.click(x, y)
                    print(f"Clicked on {image_path} at ({x}, {y})")
                    time.sleep(click_delay)  # Delay between clicks

# Main function to execute the script
def main():
    # List of image paths to search for on the screen
    # Replace these with the paths to your actual images
    image_paths = [
        r"C:\Users\aaaa\Desktop\!Python tests (mine)\images-database\test1.png",
        r"C:\Users\aaaa\Desktop\!Python tests (mine)\images-database\test2.png"
    ]

    # Call the function with the list of image paths and optional parameters
    search_and_click(image_paths)

# Entry point of the script
if __name__ == "__main__":
    main()
