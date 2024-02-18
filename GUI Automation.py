import pyautogui
import time

def automate_click(x, y, clicks=1, interval=0.5):

    pyautogui.moveTo(x, y, duration=0.5)

    for _ in range(clicks):
        pyautogui.click()
        time.sleep(interval)

#minimize the ide
automate_click(260, 740, clicks=1, interval=1)

# Define the automate_click function for clicking
def automate_click_click(x, y, clicks=1, interval=0.5):
    pyautogui.moveTo(x, y, duration=0.5)
    for _ in range(clicks):
        pyautogui.click()
        time.sleep(interval)

# Define the automate_click function for right-clicking
def automate_click_right(x, y, clicks=1, interval=0.5):
    pyautogui.moveTo(x, y, duration=0.5)
    for _ in range(clicks):
        pyautogui.click(button='right')
        time.sleep(interval)

# Define the automate_click function for clicking without specifying the button
def automate_click_no_button(x, y, clicks=1, interval=0.5):
    pyautogui.moveTo(x, y, duration=0.5)
    for _ in range(clicks):
        pyautogui.click()
        time.sleep(interval)

# Define the coordinates and intervals
coordinates = [
    (480, 350),   # Click the next page
    (1000, 400),  # Right-click
    (1020, 410),  # Right-click menu click
    (480, 480)    # Save the photo
]
intervals = [1, 1, 1, 1]  # Assuming interval 1 for all actions

# Loop through the actions
for i in range(100):
    for coord, interval, click_function in zip(coordinates, intervals, [automate_click_click, automate_click_right, automate_click_no_button, automate_click_no_button]):
        click_function(*coord, clicks=1, interval=interval)
