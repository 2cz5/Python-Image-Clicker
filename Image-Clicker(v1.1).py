# | Made by 2cz5 | https://github.com/2cz5 | Discord:2cz5 (for questions etc..)

import cv2
import numpy as np
import pyautogui
import keyboard
import time
import win32gui
import win32con

def minimize_cmd_window():
    """Minimize the command prompt window."""
    hwnd = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)

def capture_screen():
    """Capture the screen and convert it to grayscale."""
    screenshot = pyautogui.screenshot()
    screen_np = np.array(screenshot)
    return cv2.cvtColor(screen_np, cv2.COLOR_RGB2GRAY)

def find_template(image_path, screen_gray):
    """Find template matches in the screen image."""
    template = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    method = cv2.TM_CCOEFF_NORMED
    result = cv2.matchTemplate(screen_gray, template, method)
    threshold = 0.8
    loc = np.where(result >= threshold)
    return loc, template.shape[1], template.shape[0]

def click_on_matches(loc, template_width, template_height):
    """Click on the center of the matched templates."""
    for pt in zip(*loc[::-1]):
        x, y = pt[0] + template_width // 2, pt[1] + template_height // 2
        pyautogui.click(x, y)
        print(f"Clicked at ({x}, {y})")

def search_and_click(image_paths):
    """Search for images on the screen and click on them if found."""
    while True:
        minimize_cmd_window()
        if keyboard.is_pressed('q'):
            print("Killswitch activated. Exiting the loop.")
            break
        try:
            screen_gray = capture_screen()
            for image_path in image_paths:
                loc, template_width, template_height = find_template(image_path, screen_gray)
                if loc[0].size > 0:
                    click_on_matches(loc, template_width, template_height)
        except Exception as e:
            print(f"An error occurred: {e}")

# List of image paths to search for on the screen
image_paths = [
    r"C:\Users\aaaa\Desktop\!Python tests (mine)\images-database\cookie.png",
    r"C:\Users\aaaa\Desktop\!Python tests (mine)\images-database\golden.png"
]

# Call the function with the list of image paths
search_and_click(image_paths)
