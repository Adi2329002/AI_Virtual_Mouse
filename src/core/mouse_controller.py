import pyautogui
from src.config import SMOOTHENING


class MouseController:
    def __init__(self):
        pyautogui.FAILSAFE = False
        self.screen_width, self.screen_height = pyautogui.size()

        self.prev_x = 0
        self.prev_y = 0
        self.dragging = False

    def move(self, norm_x, norm_y):
        screen_x = int(norm_x * self.screen_width)
        screen_y = int(norm_y * self.screen_height)

        curr_x = self.prev_x + (screen_x - self.prev_x) / SMOOTHENING
        curr_y = self.prev_y + (screen_y - self.prev_y) / SMOOTHENING

        pyautogui.moveTo(curr_x, curr_y)

        self.prev_x, self.prev_y = curr_x, curr_y

    def left_click(self):
        pyautogui.click()

    def right_click(self):
        pyautogui.click(button="right")

    def start_drag(self):
        if not self.dragging:
            pyautogui.mouseDown()
            self.dragging = True

    def stop_drag(self):
        if self.dragging:
            pyautogui.mouseUp()
            self.dragging = False
