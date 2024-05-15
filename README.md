# Automated Image Clicking

## Showcase|Example:

https://github.com/2cz5/Python-Image-Clicker/assets/169117434/c915386e-9d5f-44ef-9988-90ca2efb501b



## Overview
This Python script is designed to automate the process of searching for specific images on the screen and clicking on them when found. It utilizes computer vision techniques to locate images and the `pyautogui` library for simulating mouse clicks.

## Features
- **Image Recognition**: Uses template matching to locate images on the screen.
- **Killswitch**: Implements a killswitch functionality to stop the script execution.
- **Logging**: Logs events and errors to a file for debugging and monitoring.
- **Customizable**: Allows customization of parameters such as threshold, click delay, and killswitch key.

## Requirements
- Python 3.x
- OpenCV (`cv2`)
- NumPy
- PyAutoGUI
- win32gui
- keyboard

## Installation
1. Clone or download the repository.
2. Install the required libraries using pip:

pip install opencv-python numpy pyautogui pypiwin32 keyboard

## Usage
1. Modify the `image_paths` list in the script to include the paths of the images you want to search for.
2. Optionally adjust parameters such as threshold, click delay, and killswitch key according to your requirements.
3. Run the script: python Image-Clicker(v1.2).py
4. Press the killswitch key (default: 'q') to stop the script execution.

## Configuration
- `threshold`: Adjusts the sensitivity of image recognition. Higher values result in stricter matching.
- `click_delay`: Specifies the delay (in seconds) between consecutive clicks.
- `killswitch_key`: Defines the key to activate the killswitch and terminate the script.

### Contributing:
Contributions are welcome! Feel free to open an issue or submit a pull request.

## Credits
- **Author**: 2cz5
- **GitHub**: [2cz5](https://github.com/2cz5)
- **Discord**: 2cz5 (for questions, feedback, etc.)
