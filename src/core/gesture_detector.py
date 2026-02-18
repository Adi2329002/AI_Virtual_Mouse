import math
import time
from src.config import CLICK_THRESHOLD, RIGHT_CLICK_THRESHOLD, CLICK_DELAY


class GestureDetector:
    def __init__(self):
        self.last_click_time = 0
        self.last_right_click_time = 0
        self.dragging = False

    def _distance(self, frame, lm1, lm2):
        h, w, _ = frame.shape
        x1, y1 = int(lm1.x * w), int(lm1.y * h)
        x2, y2 = int(lm2.x * w), int(lm2.y * h)
        return math.hypot(x2 - x1, y2 - y1)

    def detect_left_click(self, frame, hand_landmarks):
        index_tip = hand_landmarks.landmark[8]
        thumb_tip = hand_landmarks.landmark[4]

        distance = self._distance(frame, index_tip, thumb_tip)

        if distance < CLICK_THRESHOLD:
            current_time = time.time()
            if current_time - self.last_click_time > CLICK_DELAY:
                self.last_click_time = current_time
                return True
        return False

    def detect_right_click(self, frame, hand_landmarks):
        middle_tip = hand_landmarks.landmark[12]
        thumb_tip = hand_landmarks.landmark[4]

        distance = self._distance(frame, middle_tip, thumb_tip)

        if distance < RIGHT_CLICK_THRESHOLD:
            current_time = time.time()
            if current_time - self.last_right_click_time > CLICK_DELAY:
                self.last_right_click_time = current_time
                return True
        return False

    def detect_drag(self, frame, hand_landmarks):
        index_tip = hand_landmarks.landmark[8]
        thumb_tip = hand_landmarks.landmark[4]

        distance = self._distance(frame, index_tip, thumb_tip)

        if distance < CLICK_THRESHOLD:
            return True
        return False
