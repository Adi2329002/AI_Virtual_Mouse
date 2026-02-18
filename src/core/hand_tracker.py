import cv2
import mediapipe as mp
from src.config import MAX_HANDS, DETECTION_CONFIDENCE, TRACKING_CONFIDENCE


class HandTracker:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

        self.mp_hands = mp.solutions.hands
        self.mp_draw = mp.solutions.drawing_utils

        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=MAX_HANDS,
            min_detection_confidence=DETECTION_CONFIDENCE,
            min_tracking_confidence=TRACKING_CONFIDENCE
        )

    def get_frame(self):
        success, frame = self.cap.read()
        if not success:
            return None, None

        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb_frame)

        return frame, results

    def draw_landmarks(self, frame, hand_landmarks):
        self.mp_draw.draw_landmarks(
            frame,
            hand_landmarks,
            self.mp_hands.HAND_CONNECTIONS
        )

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()
