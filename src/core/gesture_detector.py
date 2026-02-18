import math
import time
from src.config import CLICK_THRESHOLD, CLICK_DELAY


class GestureDetector:
    def __init__(self):
        self.last_click_time = 0

    def detect_click(self, frame, hand_landmarks):
        """
        Returns True if click gesture detected
        """

        h, w, _ = frame.shape

        index_tip = hand_landmarks.landmark[8]
        thumb_tip = hand_landmarks.landmark[4]

        ix, iy = int(index_tip.x * w), int(index_tip.y * h)
        tx, ty = int(thumb_tip.x * w), int(thumb_tip.y * h)

        distance = math.hypot(tx - ix, ty - iy)

        if distance < CLICK_THRESHOLD:
            current_time = time.time()
            if current_time - self.last_click_time > CLICK_DELAY:
                self.last_click_time = current_time
                return True

        return False
