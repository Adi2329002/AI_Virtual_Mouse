import math
import time
from src.config import CLICK_THRESHOLD, RIGHT_CLICK_THRESHOLD, CLICK_DELAY, SCROLL_DELAY


class GestureDetector:
    def __init__(self):
        self.last_click_time = 0
        self.last_right_click_time = 0
        self.last_scroll_time = 0

        self.pinch_start_time = None
        self.prev_scroll_y = None

    def _distance(self, frame, lm1, lm2):
        h, w, _ = frame.shape
        x1, y1 = int(lm1.x * w), int(lm1.y * h)
        x2, y2 = int(lm2.x * w), int(lm2.y * h)
        return math.hypot(x2 - x1, y2 - y1)

    # ---------------- LEFT CLICK ----------------
    def detect_left_click(self, frame, hand_landmarks):
        index_tip = hand_landmarks.landmark[8]
        thumb_tip = hand_landmarks.landmark[4]

        distance = self._distance(frame, index_tip, thumb_tip)

        if distance < CLICK_THRESHOLD:
            if self.pinch_start_time is None:
                self.pinch_start_time = time.time()
            return False
        else:
            if self.pinch_start_time is not None:
                pinch_duration = time.time() - self.pinch_start_time
                self.pinch_start_time = None

                if pinch_duration < 0.25:
                    return True
        return False

    # ---------------- DRAG ----------------
    def detect_drag(self, frame, hand_landmarks):
        index_tip = hand_landmarks.landmark[8]
        thumb_tip = hand_landmarks.landmark[4]

        distance = self._distance(frame, index_tip, thumb_tip)

        if distance < CLICK_THRESHOLD:
            if self.pinch_start_time and (time.time() - self.pinch_start_time > 0.4):
                return True
        return False

    # ---------------- RIGHT CLICK ----------------
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

    # ---------------- SCROLL ----------------
    def detect_scroll(self, hand_landmarks):
        index_tip = hand_landmarks.landmark[8]
        middle_tip = hand_landmarks.landmark[12]

        avg_y = (index_tip.y + middle_tip.y) / 2

        if self.prev_scroll_y is None:
            self.prev_scroll_y = avg_y
            return 0

        delta = avg_y - self.prev_scroll_y
        self.prev_scroll_y = avg_y

        current_time = time.time()

        if current_time - self.last_scroll_time < SCROLL_DELAY:
            return 0

        if delta > 0.02:
            self.last_scroll_time = current_time
            return -1
        elif delta < -0.02:
            self.last_scroll_time = current_time
            return 1

        return 0