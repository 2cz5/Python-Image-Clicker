import cv2
import numpy as np
import pyautogui
import keyboard
import time
import win32gui
import win32con

# Function to minimize the command prompt window
def minimize_cmd_window():
    hwnd = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)

# Define a function to search for images on the screen and click on them if found
def search_and_click(images):
    # Set the template matching method
    method = cv2.TM_CCOEFF_NORMED
    
    while True:
        minimize_cmd_window()  # Minimize the command prompt window
        
        # Check if the killswitch key ('q') is pressed
        if keyboard.is_pressed('q'):
            print("Killswitch activated. Exiting the loop.")
            break

        # Capture the screen image
        screenshot = pyautogui.screenshot()
        screen_np = np.array(screenshot)
        screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_RGB2GRAY)

        # Iterate through each image in the database
        for image_path in images:
            # Load the image from the database
            template = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

            # Perform template matching
            result = cv2.matchTemplate(screen_gray, template, method)

            # Get the location of matches above a threshold
            threshold = 0.8
            loc = np.where(result >= threshold)

            # Click on the matched locations
            if loc[0].size > 0:
                for pt in zip(*loc[::-1]):
                    # Calculate the center of the matched template
                    x, y = pt[0] + template.shape[1] // 2, pt[1] + template.shape[0] // 2

                    # Click on the center of the matched template
                    while True:
                        pyautogui.click(x, y)
                        print(f"Clicked on {image_path} at ({x}, {y})")
                        # delay between clicks
                        time.sleep(1)
                        # Check if the killswitch key ('q') is pressed
                        if keyboard.is_pressed('q'):
                            print("Killswitch activated. Exiting the loop.")
                            return

# List of image paths to search for on the screen
# Replace these with the paths to your actual images
image_paths = [
    r"C:\Users\aaaa\Desktop\\!Python tests (mine)\\images-database\\test1.png",
    "C:\\Users\aaaa\Desktop\\!Python tests (mine)\\images-database\\test2.png"
]

# Call the function with the list of image paths
search_and_click(image_paths)
