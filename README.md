# Image Search and Click Automation

## Description
This Python script searches for specific images on the screen and clicks on them if found. It can be useful for automating tasks where specific images need to be located and interacted with on the screen, such as in game automation or UI testing.

## IMPORTANT NOTE:This Python code is compatible with the Windows operating system. This is because it relies on the win32gui and win32con modules, which are specific to Windows. Additionally, it utilizes the pyautogui library, which is compatible with Windows, macOS, and Linux, but the specific functionality used in this code (screen capturing and clicking) is primarily intended for Windows. Therefore, while the script may technically run on other operating systems, its functionality may be limited or behave differently on non-Windows platforms.

## Requirements
- Python 3.x
- OpenCV (`cv2`)
- NumPy (`numpy`)
- PyAutoGUI (`pyautogui`)
- Keyboard (`keyboard`)
- Win32gui (`win32gui`)
- Win32con (`win32con`)

## Usage
1. Clone the repository to your local machine. (Or click on code, then download as zip.)
2. Ensure you have all the required libraries installed. You can install them using pip: pip install opencv-python numpy pyautogui keyboard pywin32
3. Replace the paths in the `image_paths` list with the paths to your actual images.
4. Run the script using command prompt
5. Press the 'q' key to stop the script at any time.

## Notes
- Make sure the images you want to search for are available in the specified paths.
- Adjust the threshold value as needed for accurate template matching.
- This script may require adjustments based on the specific requirements of your task.


